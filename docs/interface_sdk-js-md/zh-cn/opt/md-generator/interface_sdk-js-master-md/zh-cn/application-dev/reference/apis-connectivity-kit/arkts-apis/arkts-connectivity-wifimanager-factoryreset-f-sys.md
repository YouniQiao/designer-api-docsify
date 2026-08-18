# factoryReset（系统接口）

## 导入模块

```TypeScript
```

## factoryReset

```TypeScript
function factoryReset(): void
```

重置所有已保存的设备配置。

**起始版本：** 23

**需要权限：** ohos.permission.SET_WIFI_INFO and ohos.permission.SET_WIFI_CONFIG

<!--Device-wifiManager-function factoryReset(): void--><!--Device-wifiManager-function factoryReset(): void-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [2501000](../errorcode-wifi.md#2501000-sta内部异常) |

**示例**

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

try {
  wifiManager.factoryReset();
} catch (error) {
  console.error("failed:" + JSON.stringify(error));
}
```
