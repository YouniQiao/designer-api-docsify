# isBandTypeSupported

## 导入模块

```TypeScript
```

## isBandTypeSupported

```TypeScript
function isBandTypeSupported(bandType: WifiBandType): boolean
```

检查当前设备是否支持指定频段。

**起始版本：** 23

**需要权限：** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function isBandTypeSupported(bandType: WifiBandType): boolean--><!--Device-wifiManager-function isBandTypeSupported(bandType: WifiBandType): boolean-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bandType | [WifiBandType](arkts-connectivity-wifimanager-wifibandtype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2501000](../errorcode-wifi.md#2501000-sta内部异常) |

**示例**

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let type = 0;
    let isBandTypeSupported = wifiManager.isBandTypeSupported(type);
    console.info("isBandTypeSupported:" + isBandTypeSupported);    
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```
