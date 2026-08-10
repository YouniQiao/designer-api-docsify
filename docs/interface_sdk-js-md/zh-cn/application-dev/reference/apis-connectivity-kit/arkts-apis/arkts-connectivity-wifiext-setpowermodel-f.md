# setPowerModel

## 导入模块

```TypeScript
import { wifiext } from 'kits/@kit.ConnectivityKit';
```

## setPowerModel

```TypeScript
function setPowerModel(model: PowerModel): boolean
```

Set the current Wi-Fi power mode.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** ohos.wifiManagerExt/wifiManagerExt.setPowerMode

**需要权限：** ohos.permission.MANAGE_WIFI_HOTSPOT_EXT

<!--Device-wifiext-function setPowerModel(model: PowerModel): boolean--><!--Device-wifiext-function setPowerModel(model: PowerModel): boolean-End-->

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | [PowerModel](arkts-connectivity-wifiext-powermodel-e.md) | 是 | model indicates model file description to be loaded. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns { |

