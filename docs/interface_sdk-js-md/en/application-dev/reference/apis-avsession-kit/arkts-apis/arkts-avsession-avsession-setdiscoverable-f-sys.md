# setDiscoverable (System API)

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## setDiscoverable

```TypeScript
function setDiscoverable(enable: boolean, callback: AsyncCallback<void>): void
```

设置设备是否可被发现，用于投播接收端。结果通过callback异步回调方式返回。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-function setDiscoverable(enable: boolean, callback: AsyncCallback<void>): void--><!--Device-avSession-function setDiscoverable(enable: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | 是否允许本设备被发现。true表示允许被发现，false表示不允许被发现。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当设置成功，err为undefined，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 202 | Not System App. |

## Examples

```TypeScript
avSession.setDiscoverable(true, () => {
    console.info('Succeeded in setting discoverable.');
});
```


## setDiscoverable

```TypeScript
function setDiscoverable(enable: boolean): Promise<void>
```

设置设备是否可被发现，用于投播接收端。结果通过Promise异步回调方式返回。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-function setDiscoverable(enable: boolean): Promise<void>--><!--Device-avSession-function setDiscoverable(enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | 是否允许本设备被发现。true表示允许被发现，false表示不允许被发现。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 202 | Not System App. |

## Examples

```TypeScript
avSession.setDiscoverable(true).then(() => {
  console.info('Succeeded in setting discoverable.');
});
```

