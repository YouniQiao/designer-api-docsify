# getSync

## Modules to Import

```TypeScript
import { componentSnapshot } from 'kits/@kit.ArkUI';
```

## getSync

```TypeScript
function getSync(id: string, options?: SnapshotOptions): image.PixelMap
```

Obtains the snapshot of a component that has been loaded based on the provided component ID. This API synchronously waits for the snapshot to complete and returns a [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) object.

> **NOTE：**&gt;
> The snapshot captures content rendered in the last frame. If this API is called when the component triggers an
> update, the re-rendered content will not be included in the obtained snapshot.

**Since:** 12

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
| image.PixelMap |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [160002](../errorcode-snapshot.md#160002-snapshot-timeout) |
| [160003](../errorcode-snapshot.md#160003-provided-color-space-or-dynamic-range-mode-is-not-supported) |
