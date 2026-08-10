# stopCastDeviceDiscovery (System API)

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## stopCastDeviceDiscovery

```TypeScript
function stopCastDeviceDiscovery(callback: AsyncCallback<void>): void
```

结束设备搜索发现。结果通过callback异步回调方式返回。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-function stopCastDeviceDiscovery(callback: AsyncCallback<void>): void--><!--Device-avSession-function stopCastDeviceDiscovery(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当成功停止搜索，err为undefined，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not System App. |

## Examples

```TypeScript
avSession.stopCastDeviceDiscovery(() => {
    console.info('Succeeded in stopping cast device discovery.');
});
```


## stopCastDeviceDiscovery

```TypeScript
function stopCastDeviceDiscovery(): Promise<void>
```

结束设备搜索发现。结果通过Promise异步回调方式返回。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-function stopCastDeviceDiscovery(): Promise<void>--><!--Device-avSession-function stopCastDeviceDiscovery(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当成功停止搜索，无返回结果，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not System App. |

## Examples

```TypeScript
avSession.stopCastDeviceDiscovery().then(() => {
  console.info('Succeeded in stopping cast device discovery.');
});
```

