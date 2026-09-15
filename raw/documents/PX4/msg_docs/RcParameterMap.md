---
title: "RcParameterMap (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/RcParameterMap"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/RcParameterMap.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# RcParameterMap (UORB message)

**TOPICS:** rc_parameter_map

## Fields

| Name                                    | Type         | Unit [Frame] | Range/Enum | Description                                                                                       |
| --------------------------------------- | ------------ | ------------ | ---------- | ------------------------------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp     | `uint64`     |              |            | time since system start (microseconds)                                                            |
| <a id="fld_valid"></a>valid             | `bool[3]`    |              |            | true for RC-Param channels which are mapped to a param                                            |
| <a id="fld_param_index"></a>param_index | `int32[3]`   |              |            | corresponding param index, this field is ignored if set to -1, in this case param_id will be used |
| <a id="fld_param_id"></a>param_id       | `char[51]`   |              |            | MAP_NCHAN \* (ID_LEN + 1) chars, corresponding param id, null terminated                          |
| <a id="fld_scale"></a>scale             | `float32[3]` |              |            | scale to map the RC input [-1, 1] to a parameter value                                            |
| <a id="fld_value0"></a>value0           | `float32[3]` |              |            | initial value around which the parameter value is changed                                         |
| <a id="fld_value_min"></a>value_min     | `float32[3]` |              |            | minimal parameter value                                                                           |
| <a id="fld_value_max"></a>value_max     | `float32[3]` |              |            | minimal parameter value                                                                           |

## Constants

| Name                                                | Type    | Value | Description                                                                    |
| --------------------------------------------------- | ------- | ----- | ------------------------------------------------------------------------------ |
| <a id="#RC_PARAM_MAP_NCHAN"></a> RC_PARAM_MAP_NCHAN | `uint8` | 3     | This limit is also hardcoded in the enum RC_CHANNELS_FUNCTION in rc_channels.h |
| <a id="#PARAM_ID_LEN"></a> PARAM_ID_LEN             | `uint8` | 16    | corresponds to MAVLINK_MSG_PARAM_VALUE_FIELD_PARAM_ID_LEN                      |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/RcParameterMap.msg)

::: details Click here to see original file

```c
uint64 timestamp		# time since system start (microseconds)
uint8 RC_PARAM_MAP_NCHAN = 3 # This limit is also hardcoded in the enum RC_CHANNELS_FUNCTION in rc_channels.h
uint8 PARAM_ID_LEN = 16 # corresponds to MAVLINK_MSG_PARAM_VALUE_FIELD_PARAM_ID_LEN

bool[3] valid		#true for RC-Param channels which are mapped to a param
int32[3] param_index	# corresponding param index, this field is ignored if set to -1, in this case param_id will be used
char[51] param_id	# MAP_NCHAN * (ID_LEN + 1) chars, corresponding param id, null terminated
float32[3] scale		# scale to map the RC input [-1, 1] to a parameter value
float32[3] value0		# initial value around which the parameter value is changed
float32[3] value_min	# minimal parameter value
float32[3] value_max	# minimal parameter value
```

:::
