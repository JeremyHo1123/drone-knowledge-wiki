#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate the Chinese–English glossary docs-map/glossary.md.

Why it exists: the 1,075 documents in `raw/documents/` are **all in English**, so a
Chinese search term gets zero hits. To Grep the original text you first have to
turn the Chinese term into the official English one — and pairs such as
"解鎖 → arm", "電子調速器 → ESC" or "地面站 → ground station / GCS" find nothing
at all if you guess wrong. This table fixes that translation step and checks it
against the real corpus.

The pairs (TERMS) are curated by hand, but the hit count and main locations of
every entry are computed by scanning the whole corpus. **An English term with
zero hits is listed as a miss**, so the table never contains a pair that cannot
be found. Re-run after the documents change.

Usage:
    python scripts/build-glossary.py
"""
import os
import re
import sys
from collections import Counter
from datetime import date

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "raw", "documents")

# (Chinese, [English search terms…], note)
# English terms are ordered by which one to search first; the note gives
# parameter prefixes or counter-intuitive details.
TERMS = [
    # ── Basic operations ───────────────────────────────────────
    ("解鎖 / 上鎖", ["arming", "armed", "disarm"], "Counter-intuitive: Chinese says 解鎖, the docs always use the arm root; for preflight checks see prearm"),
    ("預飛檢查", ["preflight check", "prearm"], ""),
    ("起飛", ["takeoff"], "Parameters `MIS_TAKEOFF_ALT`, `COM_` family"),
    ("降落", ["landing", "land mode"], "land detector has its own page"),
    ("返航", ["Return mode", "return to launch", "RTL"], "Parameter prefix `RTL_`"),
    ("懸停", ["hover", "hold mode"], ""),
    ("首飛", ["first flight"], ""),
    ("遙控器 / 搖桿", ["radio control", "RC", "joystick", "transmitter"], "Parameter prefixes `RC_`, `COM_RC_`"),
    ("校正", ["calibration"], "Sensor calibration is in the config/ section"),
    ("韌體燒錄", ["firmware", "flashing", "bootloader"], ""),
    ("地面站", ["ground station", "GCS", "QGroundControl"], "The QGC docs are a doc set of their own"),

    # ── Flight modes ───────────────────────────────────────────
    ("飛行模式", ["flight mode"], "Separate directories per vehicle type: flight_modes_mc / _fw / _vtol / _rover"),
    ("手動模式", ["Manual mode", "Stabilized mode"], ""),
    ("定點模式 / 定位模式", ["Position mode"], "Parameter `MPC_POS_MODE`"),
    ("定高模式", ["Altitude mode"], ""),
    ("特技模式", ["Acro mode"], ""),
    ("任務模式", ["Mission mode"], ""),
    ("機外控制 / 外部控制", ["Offboard"], "Parameters `COM_OF_LOSS_T`, `COM_OBL_RC_ACT`"),
    ("軌道模式", ["Orbit"], ""),
    ("跟隨模式", ["Follow Me"], ""),

    # ── Control and tuning ─────────────────────────────────────
    ("調參", ["tuning", "PID tuning"], "Parameter prefixes `MC_` (attitude/rate), `MPC_` (position/velocity), `FW_`"),
    ("自動調參", ["autotune", "auto-tuning"], ""),
    ("角速度控制器", ["rate controller", "angular rate"], "Innermost loop; affects all modes"),
    ("姿態控制器", ["attitude controller"], "`MC_ROLL_P` / `MC_PITCH_P` / `MC_YAW_P`"),
    ("位置控制器", ["position controller"], "`MPC_XY_P` / `MPC_Z_P`"),
    ("速度控制器", ["velocity controller"], "`MPC_XY_VEL_P_ACC` and others"),
    ("控制配置 / 混控", ["control allocation", "mixing", "mixer"], "Parameter prefix `CA_`; called mixer before v1.13"),
    ("致動器", ["actuator"], "The QGC Actuators setup screen"),
    ("最大傾角", ["tilt angle", "maximum tilt"], "`MPC_TILTMAX_AIR`"),
    ("推力曲線", ["thrust curve"], "`THR_MDL_FAC`"),
    ("濾波 / 陷波濾波器", ["notch filter", "low-pass filter", "filter tuning"], "`IMU_GYRO_NF0_FRQ`, `IMU_GYRO_CUTOFF`"),
    ("振動", ["vibration"], "Log analysis threshold: > 2–3 m/s² peak-to-peak"),
    ("配平", ["trim", "trimming"], ""),
    ("總能量控制", ["TECS", "Total Energy Control"], "Core of fixed-wing position control"),

    # ── State estimation and sensors ───────────────────────────
    ("狀態估計 / 導航濾波器", ["EKF2", "estimator", "navigation filter"], "Parameter prefix `EKF2_`"),
    ("慣性測量單元", ["IMU", "inertial measurement"], "`IMU_` prefix"),
    ("陀螺儀", ["gyroscope", "gyro"], ""),
    ("加速度計", ["accelerometer"], ""),
    ("磁力計 / 羅盤", ["magnetometer", "compass"], "Magnetic interference compensation: see compass_power_compensation"),
    ("氣壓計", ["barometer", "baro"], ""),
    ("空速", ["airspeed"], "Required for fixed-wing; `FW_AIRSPD_` prefix"),
    ("測距儀 / 高度計", ["rangefinder", "distance sensor"], ""),
    ("光流", ["optical flow"], "Velocity source when GNSS is denied"),
    ("視覺慣性里程計", ["visual inertial odometry", "VIO"], "PX4 provides only the interface; the algorithm runs on a companion computer"),
    ("動作捕捉", ["motion capture", "mocap"], ""),
    ("衛星定位", ["GNSS", "GPS"], ""),
    ("公分級定位", ["RTK"], "Needs a base + rover pair"),
    ("拒止環境 / 無 GPS", ["GNSS-denied", "GPS-denied", "degraded"], ""),
    ("地形跟隨", ["terrain following", "terrain hold"], ""),

    # ── Safety ─────────────────────────────────────────────────
    ("失效保護", ["failsafe"], "Parameter prefix `COM_`; the QGC Safety page"),
    ("地理圍欄", ["geofence"], "Parameter prefix `GF_`; active in all modes"),
    ("返航點", ["rally point"], "Part of the same Plan as the mission and the fence"),
    ("飛行終止", ["flight termination"], "The most severe failsafe action; can deploy a parachute"),
    ("降落傘", ["parachute"], "Triggered through the flight termination PWM failsafe values"),
    ("電池 / 電量", ["battery"], "Parameter prefix `BAT_`"),
    ("失控保護 / 訊號中斷", ["RC loss", "link loss", "datalink loss"], "`COM_RC_LOSS_T`, `COM_DL_LOSS_T`"),
    ("避障", ["obstacle avoidance", "path planning"], "Actively routes around obstacles; needs a companion computer"),
    ("防撞", ["collision prevention"], "Only slows and stops, never routes around; parameter prefix `CP_`"),
    ("落地偵測", ["land detector"], ""),

    # ── Missions and navigation ────────────────────────────────
    ("任務 / 航線", ["mission", "waypoint"], "Parameter prefixes `MIS_`, `NAV_`"),
    ("航點", ["waypoint"], "`MAV_CMD_NAV_WAYPOINT`"),
    ("測繪 / 掃描", ["survey", "corridor scan", "structure scan"], "The QGC Pattern tools"),
    ("軌跡", ["trajectory"], "`TrajectorySetpoint` uORB topic"),
    ("航向", ["heading", "yaw"], "When a mission item has no Heading, `MPC_YAW_MODE` decides"),
    ("精準降落", ["precision landing"], ""),
    ("投遞 / 酬載", ["payload", "package delivery", "cargo"], ""),
    ("雲台", ["gimbal"], "MAVSDK has a gimbal plugin"),
    ("相機", ["camera"], ""),

    # ── Communication and integration ──────────────────────────
    ("遙測 / 數傳", ["telemetry"], "MAVSDK has a telemetry plugin"),
    ("訊息匯流排", ["uORB"], "`uorb top`, `listener` commands"),
    ("訊息定義", ["message", "msg", "topic"], "raw/documents/PX4/msg_docs/ has 284 pages"),
    ("串列埠", ["serial", "UART"], "Parameter prefix `SER_`"),
    ("乙太網路", ["ethernet"], ""),
    ("機載電腦", ["companion computer"], "Jetson, Raspberry Pi and others"),
    ("ROS 整合", ["ROS 2", "uXRCE-DDS", "MAVROS"], "uXRCE-DDS replaced Fast-RTPS from v1.14"),
    ("模組 / 指令", ["module", "command"], "raw/documents/PX4/modules/"),
    ("參數", ["parameter"], "The full table is in advanced_config/parameter_reference"),

    # ── Hardware ───────────────────────────────────────────────
    ("飛控板", ["flight controller", "Pixhawk"], "66 board pages"),
    ("電子調速器", ["ESC", "electronic speed controller"], "Counter-intuitive: Chinese often says 電調, the docs always say ESC"),
    ("馬達", ["motor"], ""),
    ("舵機", ["servo"], ""),
    ("機體 / 機架", ["airframe", "frame"], "The QGC Airframe setup"),
    ("多旋翼", ["multicopter", "multirotor"], "Sections flight_modes_mc / config_mc"),
    ("固定翼", ["fixed-wing", "plane"], "Sections flight_modes_fw / config_fw"),
    ("垂直起降", ["VTOL"], "Parameter prefix `VT_`"),
    ("直升機", ["helicopter"], ""),
    ("無人車 / 無人船", ["rover", "boat"], ""),
    ("電源模組", ["power module"], ""),
    ("智慧電池", ["smart battery"], ""),

    # ── Development, simulation, debugging ─────────────────────
    ("模擬", ["simulation", "SITL", "HITL"], "Gazebo (new) / SIH (lightweight) / Gazebo Classic (demoted)"),
    ("編譯 / 建置", ["building", "build"], "dev_setup section"),
    ("開發環境", ["development environment", "dev_env", "toolchain"], "Section `PX4/dev_setup`"),
    ("除錯", ["debugging", "console"], "debug section"),
    ("飛行記錄", ["flight log", "ULog", "logging"], "Parameter prefix `SDLOG_`"),
    ("記錄分析", ["log analysis", "Flight Review", "PlotJuggler"], "logs.px4.io"),
    ("單元測試 / CI", ["unit test", "continuous integration"], ""),
    ("自訂機體設定", ["adding a new frame", "airframe configuration"], ""),

    # ── MAVSDK specific ────────────────────────────────────────
    ("連線位址", ["system_address", "udpin", "connect"], "SITL default `udpin://0.0.0.0:14540`"),
    ("外掛 / plugin", ["plugin"], "One page per MAVSDK plugin"),
    ("非同步訂閱", ["async", "Yields", "subscribe"], "Telemetry methods return async generators"),
]


def main():
    # Read the whole corpus once; every term is then matched in memory
    corpus = []
    for dirpath, _, files in os.walk(DOCS):
        for f in files:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dirpath, f)
            rel = os.path.relpath(p, DOCS).replace("\\", "/")
            try:
                text = open(p, encoding="utf-8-sig", errors="replace").read().lower()
            except Exception:                                    # noqa: BLE001
                continue
            corpus.append((rel, text))
    print(f"Corpus: {len(corpus)} documents")

    rows, misses = [], []
    for zh, ens, hint in TERMS:
        best = []
        for en in ens:
            # Match on word boundaries, not substrings: `ESC` would otherwise hit
            # describe / escape and inflate 29 documents to 700, which makes the
            # whole table useless. Underscores and hyphens count as boundaries,
            # so esc_calibration still counts as a hit.
            pat = re.compile(r"(?<![a-z0-9])" + re.escape(en.lower()) + r"(?![a-z0-9])")
            hits = [rel for rel, text in corpus if pat.search(text)]
            if not hits:
                misses.append((zh, en))
                continue
            secs = Counter(r.split("/")[0] + "/" + (r.split("/")[1] if "/" in r[r.index("/") + 1:] else "")
                           for r in hits)
            top = ", ".join(f"`{s.rstrip('/')}`" for s, _ in secs.most_common(3))
            best.append((en, len(hits), top))
        if best:
            rows.append((zh, best, hint))

    today = date.today().isoformat()
    out = [
        "---",
        'title: "Chinese–English glossary"',
        "type: docs-index",
        f"generated: {today}",
        "tags:",
        "  - docs/index",
        "---",
        "",
        "# Chinese–English glossary",
        "",
        "The documents in `raw/documents/` are **all in English**, so Chinese search terms get zero hits. "
        "This table maps Chinese phrasings to the official English terms, with the number of documents "
        "each term really appears in and where it mostly appears, so a single Grep finds the right text.",
        "",
        "> [!important] For retrieval",
        "> When a technical question is asked in Chinese, **translate the key terms with this table before you Grep**.",
        "> The \"Hits\" column is the number of documents (out of "
        f"{len(corpus)}) that contain the English term as a whole word. A large number (>150) means the term is too broad:",
        "> add a qualifier, or narrow the Grep `path` with the \"Main locations\" column.",
        "",
        f"Generated by `scripts/build-glossary.py` ({today}). The Chinese–English pairs are curated by hand; "
        "hit counts and locations are computed from the corpus. Re-run after the documents change.",
        "",
        "| Chinese | Official term (search term) | Hits | Main locations | Notes |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for zh, best, hint in rows:
        first = True
        for en, n, top in best:
            out.append(f"| {zh if first else ''} | `{en}` | {n} | {top} | {hint if first else ''} |")
            first = False
    out.append("")

    if misses:
        out.append("## Terms with no hits in the corpus")
        out.append("")
        out.append("These pairs have zero hits in the current corpus — upstream may have changed the wording, "
                   "or the pair is wrong. **Don't search with these terms.**")
        out.append("")
        for zh, en in misses:
            out.append(f"- {zh} → `{en}`")
        out.append("")

    p = os.path.join(ROOT, "docs-map", "glossary.md")
    open(p, "w", encoding="utf-8", newline="\n").write("\n".join(out))
    print(f"  {p} ({len(rows)} Chinese terms, {sum(len(b) for _, b, _ in rows)} search terms, "
          f"{len(misses)} with no hits)")


if __name__ == "__main__":
    main()
