# KeyProcessingMode

Key processing mode.Determines the priority of key event processing when component cannot handle the key event.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare enum KeyProcessingMode--><!--Device-unnamed-export declare enum KeyProcessingMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## FOCUS_NAVIGATION

```TypeScript
FOCUS_NAVIGATION = 0
```

Key events are used to move focus.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-KeyProcessingMode-FOCUS_NAVIGATION = 0--><!--Device-KeyProcessingMode-FOCUS_NAVIGATION = 0-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## ANCESTOR_EVENT

```TypeScript
ANCESTOR_EVENT = 1
```

Key events bubble up to ancestors.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-KeyProcessingMode-ANCESTOR_EVENT = 1--><!--Device-KeyProcessingMode-ANCESTOR_EVENT = 1-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

