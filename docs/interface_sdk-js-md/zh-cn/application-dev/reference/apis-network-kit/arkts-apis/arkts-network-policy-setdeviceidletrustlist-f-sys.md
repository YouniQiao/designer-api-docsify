# setDeviceIdleTrustlist（系统接口）

## 导入模块

```TypeScript
import { policy } from 'kits/@kit.NetworkKit';
```

## setDeviceIdleTrustlist

```TypeScript
function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean, callback: AsyncCallback<void>): void
```

Set the list of uids that are allowed to access the Internet in hibernation mode.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**需要权限：** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean, callback: AsyncCallback<void>): void--><!--Device-policy-function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uids | Array&lt;number&gt; | 是 | The specified uids of application. |
| isAllowed | boolean | 是 | Whether to allow Uids in the list to access the Internet. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | the callback of setDeviceIdleTrustlist. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

policy.setDeviceIdleTrustlist([11111, 22222], true, (error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```


## setDeviceIdleTrustlist

```TypeScript
function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean): Promise<void>
```

Set the list of uids that are allowed to access the Internet in hibernation mode.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**需要权限：** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean): Promise<void>--><!--Device-policy-function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uids | Array&lt;number&gt; | 是 | The specified uids of application. |
| isAllowed | boolean | 是 | Whether to allow Uids in the list to access the Internet. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

policy
  .setDeviceIdleTrustlist([11111, 22222], true)
  .then(() => {
    console.info('setDeviceIdleTrustlist success');
  })
  .catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
  });
```

