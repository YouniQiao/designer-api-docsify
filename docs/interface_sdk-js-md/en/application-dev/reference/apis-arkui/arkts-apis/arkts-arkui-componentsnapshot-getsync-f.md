# getSync

## Modules to Import

```TypeScript
import { componentSnapshot } from 'componentSnapshot';
```

## getSync

```TypeScript
export function getSync(id: string, options?: SnapshotOptions): image.PixelMap | null
```

Take a screenshot of the specified component in synchronous mode, this mode will block the main thread, please use it with caution, the maximum waiting time of the interface is 3s, if it does not return after 3s, an exception will be thrown.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-componentSnapshot-export function getSync(id: string, options?: SnapshotOptions): image.PixelMap | null--><!--Device-componentSnapshot-export function getSync(id: string, options?: SnapshotOptions): image.PixelMap | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | Target component ID, set by developer through .id attribute. |
| options | [SnapshotOptions](arkts-arkui-componentsnapshot-snapshotoptions-i.md) | No | Define the snapshot options. |

**Return value:**

| Type | Description |
| --- | --- |
| image.PixelMap | The snapshot result in PixelMap format. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../errorcode-internal.md#100001-internal-error) | Invalid ID. |
| [160002](../errorcode-snapshot.md#160002-snapshot-timeout) | Timeout. |
| [160003](../errorcode-snapshot.md#160003-provided-color-space-or-dynamic-range-mode-is-not-supported) | Unsupported color space or dynamic range mode in snapshot options. |

