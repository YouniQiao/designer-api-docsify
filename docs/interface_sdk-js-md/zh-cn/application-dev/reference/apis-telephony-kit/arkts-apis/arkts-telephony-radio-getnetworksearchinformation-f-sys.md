# getNetworkSearchInformation（系统接口）

## 导入模块

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## getNetworkSearchInformation

```TypeScript
function getNetworkSearchInformation(slotId: int, callback: AsyncCallback<NetworkSearchResult>): void
```

Get network search information.

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-radio-function getNetworkSearchInformation(slotId: int, callback: AsyncCallback<NetworkSearchResult>): void--><!--Device-radio-function getNetworkSearchInformation(slotId: int, callback: AsyncCallback<NetworkSearchResult>): void-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;NetworkSearchResult&gt; | 是 | Indicates the callback for getting the search results of the network. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

radio.getNetworkSearchInformation(0, (err: BusinessError, data: radio.NetworkSearchResult) => {
    if (err) {
        console.error(`getNetworkSearchInformation failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.info(`getNetworkSearchInformation success, callback: data->${JSON.stringify(data)}`);
});
```


## getNetworkSearchInformation

```TypeScript
function getNetworkSearchInformation(slotId: int): Promise<NetworkSearchResult>
```

Get network search information.

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-radio-function getNetworkSearchInformation(slotId: int): Promise<NetworkSearchResult>--><!--Device-radio-function getNetworkSearchInformation(slotId: int): Promise<NetworkSearchResult>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;NetworkSearchResult&gt; | Returns the search results of the network. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

radio.getNetworkSearchInformation(0).then((data: radio.NetworkSearchResult) => {
    console.info(`getNetworkSearchInformation success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getNetworkSearchInformation failed, promise: err->${JSON.stringify(err)}`);
});
```

