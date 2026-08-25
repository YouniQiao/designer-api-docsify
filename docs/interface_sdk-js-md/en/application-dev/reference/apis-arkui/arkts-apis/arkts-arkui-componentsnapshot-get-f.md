# get

## Modules to Import

```TypeScript
import { componentSnapshot } from 'kits/@kit.ArkUI';
```

## get

```TypeScript
function get(id: string, callback: AsyncCallback<image.PixelMap>, options?: SnapshotOptions): void
```

Obtains the snapshot of a component that has been loaded based on the provided component ID. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - Since API version 12, you can use the [getComponentSnapshot](arkts-arkui-arkui-uicontext-uicontext-c.md#getcomponentsnapshot)
> API in [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [ComponentSnapshot](arkts-arkui-arkui-uicontext-componentsnapshot-c.md)
> object associated with the current UI context.&gt;
> - The snapshot captures content rendered in the last frame. If this API is called when the component triggers an
> update, the re-rendered content will not be included in the obtained snapshot.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** get

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |
| options | [SnapshotOptions](arkts-arkui-componentsnapshot-snapshotoptions-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |


## get

```TypeScript
function get(id: string, options?: SnapshotOptions): Promise<image.PixelMap>
```

Obtains the snapshot of a component that has been loaded based on the provided component ID. This API uses a promise to return the result.

> **NOTE：**&gt;
> - Since API version 12, you can use the [getComponentSnapshot](arkts-arkui-arkui-uicontext-uicontext-c.md#getcomponentsnapshot)
> API in [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [ComponentSnapshot](arkts-arkui-arkui-uicontext-componentsnapshot-c.md)
> object associated with the current UI context.&gt;
> - The snapshot captures content rendered in the last frame. If this API is called when the component triggers an
> update, the re-rendered content will not be included in the obtained snapshot.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** get

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |
| options | [SnapshotOptions](arkts-arkui-componentsnapshot-snapshotoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
