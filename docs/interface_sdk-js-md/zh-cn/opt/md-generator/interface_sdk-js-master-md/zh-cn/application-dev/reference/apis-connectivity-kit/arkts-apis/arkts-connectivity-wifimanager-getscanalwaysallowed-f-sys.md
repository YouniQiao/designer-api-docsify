# getScanAlwaysAllowed（系统接口）

## 导入模块

```TypeScript
```

## getScanAlwaysAllowed

```TypeScript
function getScanAlwaysAllowed(): boolean
```

获取是否始终允许扫描。

**起始版本：** 23

**需要权限：** ohos.permission.GET_WIFI_INFO and ohos.permission.GET_WIFI_CONFIG

<!--Device-wifiManager-function getScanAlwaysAllowed(): boolean--><!--Device-wifiManager-function getScanAlwaysAllowed(): boolean-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

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
    let isScanAlwaysAllowed = wifiManager.getScanAlwaysAllowed();
    console.info("isScanAlwaysAllowed:" + isScanAlwaysAllowed);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```
