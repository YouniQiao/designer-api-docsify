# offDragStateChange (System API)

## Modules to Import

```TypeScript
```

## offDragStateChange

```TypeScript
function offDragStateChange(callback?: Callback<DragState>): void
```

Disables listening for dragging state change events.

**Since:** 23

<!--Device-dragInteraction-function offDragStateChange(callback?: Callback<DragState>): void--><!--Device-dragInteraction-function offDragStateChange(callback?: Callback<DragState>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Drag

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DragState](arkts-arkui-draginteraction-dragstate-e-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
