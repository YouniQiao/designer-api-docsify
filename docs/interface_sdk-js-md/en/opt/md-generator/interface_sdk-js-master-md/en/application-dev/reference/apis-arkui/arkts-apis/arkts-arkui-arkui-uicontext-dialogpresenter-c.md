# DialogPresenter

Provides unified dialog APIs.

**Since:** 26.1.0

<!--Device-unnamed-export class DialogPresenter--><!--Device-unnamed-export class DialogPresenter-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CustomKeyboardContinueFeature, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from '@kit.ArkUI';
```

## dismiss

```TypeScript
dismiss(target: number | ComponentContent<Object>): Promise<void>
```

Dismisses a dialog box.Accepts either the dialog ID (returned by present) or the ComponentContent reference.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogPresenter-dismiss(target: int | ComponentContent<Object>): Promise<void>--><!--Device-DialogPresenter-dismiss(target: int | ComponentContent<Object>): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | number \| ComponentContent & lt;Object & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [103301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-promptAction.md#103301-dialog-content-error) |
| [103303](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-promptAction.md#103303-custom-dialog-box-not-found) |

## present

```TypeScript
present(options?: dialog.DialogStyleOptions): Promise<DialogResult>
```

Presents a fixed-style dialog box.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogPresenter-present(options?: dialog.DialogStyleOptions): Promise<DialogResult>--><!--Device-DialogPresenter-present(options?: dialog.DialogStyleOptions): Promise<DialogResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | dialog.DialogStyleOptions | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DialogResult](arkts-arkui-arkui-dialog-dialogresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 103306 |
| 103308 |

## present

```TypeScript
present(content: CustomBuilder | CustomBuilderWithId | ComponentContent<Object>, options?: dialog.DialogCustomOptions): Promise<DialogResult>
```

Presents a custom-style dialog box with the provided content.

The content parameter accepts CustomBuilder or ComponentContent via union type:  
- CustomBuilder: Builder function for custom dialog content.  
- ComponentContent: ComponentContent supporting state-driven updates.

isModal = true and showInSubWindow = true cannot be used at the same time.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogPresenter-present(content: CustomBuilder | CustomBuilderWithId | ComponentContent<Object>, options?: dialog.DialogCustomOptions): Promise<DialogResult>--><!--Device-DialogPresenter-present(content: CustomBuilder | CustomBuilderWithId | ComponentContent<Object>, options?: dialog.DialogCustomOptions): Promise<DialogResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| [CustomBuilderWithId](arkts-arkui-custombuilderwithid-t.md) \| ComponentContent & lt;Object & gt; | Yes |
| options | dialog.DialogCustomOptions | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DialogResult](arkts-arkui-arkui-dialog-dialogresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [103301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-promptAction.md#103301-dialog-content-error) |
| [103302](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-promptAction.md#103302-custom-dialog-box-already-exists) |
| 103306 |
| 103308 |

## update

```TypeScript
update(content: ComponentContent<Object>, options?: dialog.DialogBaseOptions): Promise<void>
```

Updates a presented custom dialog box.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogPresenter-update(content: ComponentContent<Object>, options?: dialog.DialogBaseOptions): Promise<void>--><!--Device-DialogPresenter-update(content: ComponentContent<Object>, options?: dialog.DialogBaseOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | ComponentContent & lt;Object & gt; | Yes |
| options | dialog.DialogBaseOptions | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [103301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-promptAction.md#103301-dialog-content-error) |
| [103303](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-promptAction.md#103303-custom-dialog-box-not-found) |
