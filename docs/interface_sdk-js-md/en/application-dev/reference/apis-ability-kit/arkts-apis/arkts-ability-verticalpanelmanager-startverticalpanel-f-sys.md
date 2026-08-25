# startVerticalPanel (System API)

## Modules to Import

```TypeScript
import { verticalPanelManager } from 'kits/@kit.AbilityKit';
```

## startVerticalPanel

```TypeScript
function startVerticalPanel(
      context: common.UIAbilityContext,
      wantParam: Record<string, Object>,
      panelConfig: PanelConfig,
      panelStartCallback: PanelStartCallback
  ): Promise<void>
```

Starts the vertical domain picker with panel config. If the target ability is visible, you can start the target ability; If the target ability is invisible, you need to apply for permission:ohos.permission.START_INVISIBLE_ABILITY to start target invisible ability. If the caller application is in the background, it is not allowed to call this interface.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AppExtension.VerticalPanel

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | common.UIAbilityContext | Yes |
| wantParam | Record & lt;string, Object & gt; | Yes |
| panelConfig | [PanelConfig](arkts-ability-verticalpanelmanager-panelconfig-i-sys.md) | Yes |
| panelStartCallback | [PanelStartCallback](arkts-ability-verticalpanelmanager-panelstartcallback-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000135](../errorcode-ability.md#16000135-uiability-main-window-does-not-exist) |
