# isSharingSupported（系统接口）

## 导入模块

```TypeScript
import { sharing } from 'kits/@kit.NetworkKit';
```

## isSharingSupported

```TypeScript
function isSharingSupported(callback: AsyncCallback<boolean>): void
```

Checks whether this device allows for network sharing.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function isSharingSupported(callback: AsyncCallback<boolean>): void--><!--Device-sharing-function isSharingSupported(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetSharing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 | Returns {@code true} indicating network sharing is supported; returns {@code false} otherwise. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2200003 | System internal error. |
| 2200002 | Failed to connect to the service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 2202011 | Cannot get network sharing configuration. |

## 示例

```TypeScript
import { sharing } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

sharing.isSharingSupported((error: BusinessError, data: boolean) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});
```


## isSharingSupported

```TypeScript
function isSharingSupported(): Promise<boolean>
```

Checks whether this device allows for network sharing.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function isSharingSupported(): Promise<boolean>--><!--Device-sharing-function isSharingSupported(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetSharing

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2200003 | System internal error. |
| 2200002 | Failed to connect to the service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 2202011 | Cannot get network sharing configuration. |

## 示例

```TypeScript
import { sharing } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

sharing
  .isSharingSupported()
  .then((data: boolean) => {
    console.info(JSON.stringify(data));
  })
  .catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
  });
```

