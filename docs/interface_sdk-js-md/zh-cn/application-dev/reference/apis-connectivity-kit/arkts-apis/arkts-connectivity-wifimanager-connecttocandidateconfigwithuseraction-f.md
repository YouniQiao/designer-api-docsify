# connectToCandidateConfigWithUserAction

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## connectToCandidateConfigWithUserAction

```TypeScript
function connectToCandidateConfigWithUserAction(networkId: int): Promise<void>
```

Connect to a specified candidate hotspot by networkId, and wait for user respond result.Only the configuration which is added by ourself is allowed to be connected.This method connect to a configuration at a time.The app must be in the foreground.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.SET_WIFI_INFO

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-wifiManager-function connectToCandidateConfigWithUserAction(networkId: int): Promise<void>--><!--Device-wifiManager-function connectToCandidateConfigWithUserAction(networkId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Network ID which will be connected. The value of networkId cannot be less than 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Returns the promise object that used to return the operation result. If the operation fails, an error message is returned. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 2501006 | The user refused the action. |
| 201 | Permission denied. |
| 2501007 | Parameter validation failed. |
| 2501005 | The user does not respond. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

## 示例

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
  
  try {
    let networkId = 0; // 候选网络ID，在添加候选网络时生成
    wifiManager.connectToCandidateConfigWithUserAction(networkId).then(result => {
      console.info("result:" + JSON.stringify(result));
    }).catch((err:number) => {
      console.error("failed:" + JSON.stringify(err));
    });
  }catch(error){  
    console.error("failed:" + JSON.stringify(error));
  }
```

