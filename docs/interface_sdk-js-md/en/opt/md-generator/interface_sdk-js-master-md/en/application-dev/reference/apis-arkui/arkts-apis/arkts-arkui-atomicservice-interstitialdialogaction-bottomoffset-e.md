# BottomOffset

Defines the distance between the popup and the bottom in different scenario modes, based on the presence or absence of a menu bar, with the default being the distance when there is no menu bar.

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Value](../../apis-arkdata/arkts-apis/arkts-arkdata-distributeddata-value-i.md) | Description|
| - | - | - |
| [OFFSET_FOR_BAR](arkts-arkui-atomicservice-interstitialdialogaction-bottomoffset-e.md) | 0 | Distance from the bottom of the window when there is a menu bar.It sets the dialog box 88 vp away from the bottom of the window.|
| [OFFSET_FOR_NONE](arkts-arkui-atomicservice-interstitialdialogaction-bottomoffset-e.md) | 1 |

**Since:** 12

<!--Device-unnamed-export declare enum BottomOffset--><!--Device-unnamed-export declare enum BottomOffset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## OFFSET_FOR_BAR

```TypeScript
OFFSET_FOR_BAR = 0
```

dialog distance relative to the bottom in the presence of tabs.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BottomOffset-OFFSET_FOR_BAR = 0--><!--Device-BottomOffset-OFFSET_FOR_BAR = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## OFFSET_FOR_NONE

```TypeScript
OFFSET_FOR_NONE = 1
```

dialog is the distance relative to the bottom without tabs.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BottomOffset-OFFSET_FOR_NONE = 1--><!--Device-BottomOffset-OFFSET_FOR_NONE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
