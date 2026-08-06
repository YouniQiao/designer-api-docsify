# KeyPressedConfig

Sets the key event consumption configuration.

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-inputConsumer-interface KeyPressedConfig--><!--Device-inputConsumer-interface KeyPressedConfig-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## action

```TypeScript
action: int
```

Subscription type.

**Note**: Since API version 21, the value of this parameter can be **1** or **2**. The value **1** indicates subscription to only key press events, and the value **2** indicates subscription to both key press and release events.

In API version 20 or earlier versions, the value of this parameter can only be set to **1**, indicating subscription to only key press events.

**Type:** int

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-KeyPressedConfig-action: int--><!--Device-KeyPressedConfig-action: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## isRepeat

```TypeScript
isRepeat: boolean
```

Whether to report repeated key events. The value **true** means to report repeated key events, and the value  
**false** means the opposite. The default value is **true**.

**Type:** boolean

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-KeyPressedConfig-isRepeat: boolean--><!--Device-KeyPressedConfig-isRepeat: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## key

```TypeScript
key: int
```

Key value.

**Note:** Since API version 26.0.0, the  
[KEYCODE\_FINGERPRINT\_SLIDE\_UP]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ and  
[KEYCODE\_FINGERPRINT\_SLIDE\_DOWN]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ keys are supported. The keys are not universal device keys. Before using them, check whether the current device supports the reporting of related key events. For details, see  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

Since API version 21, the [KEYCODE\_MEDIA\_PLAY\_PAUSE]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_,  
[KEYCODE\_MEDIA\_NEXT]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_, and  
[KEYCODE\_MEDIA\_PREVIOUS]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ keys are supported.

In API version 20 or earlier versions, only the [KEYCODE\_VOLUME\_UP]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_and [KEYCODE\_VOLUME\_DOWN]\_\_\_JSDOC\_LINK\_DESC\_USD\_7\_\_\_ keys are supported.

**Type:** int

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-KeyPressedConfig-key: int--><!--Device-KeyPressedConfig-key: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

