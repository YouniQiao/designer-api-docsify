# getSharingIfaces（系统接口）

## 导入模块

```TypeScript
import { sharing } from 'kits/@kit.NetworkKit';
```

## getSharingIfaces

```TypeScript
function getSharingIfaces(state: SharingIfaceState, callback: AsyncCallback<Array<string>>): void
```

Obtains the names of interfaces in each sharing state.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function getSharingIfaces(state: SharingIfaceState, callback: AsyncCallback<Array<string>>): void--><!--Device-sharing-function getSharingIfaces(state: SharingIfaceState, callback: AsyncCallback<Array<string>>): void-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetSharing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [SharingIfaceState](arkts-network-sharing-sharingifacestate-e-sys.md) | 是 | Is the network sharing state. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 | Returns an array of interface names that meet this status. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2200001 | Invalid parameter value. |
| 401 | Parameter error. |
| 2200003 | System internal error. |
| 2200002 | Failed to connect to the service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

## 示例

```TypeScript
import { sharing } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let SHARING_BLUETOOTH = 2;
sharing.getSharingIfaces(SHARING_BLUETOOTH, (error: BusinessError, data: string[]) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});
```


## getSharingIfaces

```TypeScript
function getSharingIfaces(state: SharingIfaceState): Promise<Array<string>>
```

Obtains the names of interfaces in each sharing state.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function getSharingIfaces(state: SharingIfaceState): Promise<Array<string>>--><!--Device-sharing-function getSharingIfaces(state: SharingIfaceState): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetSharing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [SharingIfaceState](arkts-network-sharing-sharingifacestate-e-sys.md) | 是 | Is the network sharing state. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2200001 | Invalid parameter value. |
| 401 | Parameter error. |
| 2200003 | System internal error. |
| 2200002 | Failed to connect to the service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

## 示例

```TypeScript
import { sharing } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let SHARING_BLUETOOTH = 2;
sharing
  .getSharingIfaces(SHARING_BLUETOOTH)
  .then((data: string[]) => {
    console.info(JSON.stringify(data));
  })
  .catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
  });
```

