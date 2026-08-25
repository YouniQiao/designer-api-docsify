# setPowerModel

## 导入模块

```TypeScript
import { wifiext } from '@kit.ConnectivityKit';
```

## setPowerModel

```TypeScript
function setPowerModel(model: PowerModel): boolean
```

设置功率模式。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [setPowerMode](arkts-connectivity-wifimanagerext-setpowermode-f.md)

**需要权限：** ohos.permission.MANAGE_WIFI_HOTSPOT_EXT

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| model | [PowerModel](arkts-connectivity-wifiext-powermodel-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
