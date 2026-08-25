# isWlanSupported

## 导入模块

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## isWlanSupported

```TypeScript
function isWlanSupported(): boolean
```

查询WLAN是否可用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.WiFi.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [2401000](../errorcode-wifi.md#2401000-sta内部异常) |
