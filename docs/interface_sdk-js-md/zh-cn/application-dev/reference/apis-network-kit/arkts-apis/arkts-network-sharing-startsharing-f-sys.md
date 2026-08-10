# startSharing（系统接口）

## 导入模块

```TypeScript
import { sharing } from 'kits/@kit.NetworkKit';
```

## startSharing

```TypeScript
function startSharing(type: SharingIfaceType, callback: AsyncCallback<void>): void
```

Start network sharing for given type.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function startSharing(type: SharingIfaceType, callback: AsyncCallback<void>): void--><!--Device-sharing-function startSharing(type: SharingIfaceType, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetSharing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SharingIfaceType](arkts-network-sharing-sharingifacetype-e-sys.md) | 是 | Enumeration of shareable interface types. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | the callback of startSharing. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2200001 | Invalid parameter value. |
| 401 | Parameter error. |
| 2200003 | System internal error. |
| 2200002 | Failed to connect to the service. |
| 2202005 | WiFi sharing failed. |
| 2202004 | Try to share an unavailable iface. |
| 2202006 | Bluetooth sharing failed. |
| 2202009 | Failed to enable forwarding for network sharing. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 2202011 | Cannot get network sharing configuration. |

## 示例

```TypeScript
import { sharing } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let SHARING_WIFI = 0;
sharing.startSharing(SHARING_WIFI, (error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```


## startSharing

```TypeScript
function startSharing(type: SharingIfaceType): Promise<void>
```

Start network sharing for given type.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function startSharing(type: SharingIfaceType): Promise<void>--><!--Device-sharing-function startSharing(type: SharingIfaceType): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetSharing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SharingIfaceType](arkts-network-sharing-sharingifacetype-e-sys.md) | 是 | Enumeration of shareable interface types. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2200001 | Invalid parameter value. |
| 401 | Parameter error. |
| 2200003 | System internal error. |
| 2200002 | Failed to connect to the service. |
| 2202005 | WiFi sharing failed. |
| 2202004 | Try to share an unavailable iface. |
| 2202006 | Bluetooth sharing failed. |
| 2202009 | Failed to enable forwarding for network sharing. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 2202011 | Cannot get network sharing configuration. |

## 示例

```TypeScript
import { sharing } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let SHARING_WIFI = 0;
sharing
  .startSharing(SHARING_WIFI)
  .then(() => {
    console.info('start wifi sharing successful');
  })
  .catch((error: BusinessError) => {
    console.error('start wifi sharing failed');
  });
```

