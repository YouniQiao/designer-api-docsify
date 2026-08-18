# getSupportedFeatures（系统接口）

## 导入模块

```TypeScript
```

## getSupportedFeatures

```TypeScript
function getSupportedFeatures(): number
```

查询设备支持的特性。 检查此设备是否支持指定特性。

**起始版本：** 23

**需要权限：** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function getSupportedFeatures(): long--><!--Device-wifiManager-function getSupportedFeatures(): long-End-->

**系统能力：** SystemCapability.Communication.WiFi.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [2401000](../errorcode-wifi.md#2401000-sta内部异常) |

**示例**

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

try {
    let ret = wifiManager.getSupportedFeatures();
    console.info("supportedFeatures:" + ret);
} catch (error) {
    console.error("failed:" + JSON.stringify(error));
}
```
