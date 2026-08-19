# ComponentSnapshot

class ComponentSnapshot

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class ComponentSnapshot--><!--Device-unnamed-export declare class ComponentSnapshot-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## getWithRange

```TypeScript
getWithRange(start: NodeIdentity, end: NodeIdentity, isStartRect: boolean,
    options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null
```

Get a component snapshot by component range.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentSnapshot-getWithRange(start: NodeIdentity, end: NodeIdentity, isStartRect: boolean,    options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null--><!--Device-ComponentSnapshot-getWithRange(start: NodeIdentity, end: NodeIdentity, isStartRect: boolean,    options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | [NodeIdentity](../../apis-arkui/arkts-apis/arkts-arkui-nodeidentity-t.md) | Yes | the start component ID, set by developer through .id attribute or the unique ID get from FrameNode. |
| end | [NodeIdentity](../../apis-arkui/arkts-apis/arkts-arkui-nodeidentity-t.md) | Yes | the end component ID, set by developer through.id attribute or the unique ID get from FrameNode. |
| isStartRect | boolean | Yes | indicating the snapshot rect to use, true for using the rect of the start component, false for using the rect of the end component. |
| options | componentSnapshot.SnapshotOptions | No | Define the snapshot options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | A Promise with the snapshot in PixelMap format. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Invalid ID detected. |
| [160003](../../apis-arkui/errorcode-snapshot.md#160003-provided-color-space-or-dynamic-range-mode-is-not-supported) | Unsupported color space or dynamic range mode in snapshot options. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |

