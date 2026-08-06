# FullScreenLaunchComponent

FullScreenLaunchComponent** is a component designed for launching atomic services in full screen. If the invoked app (the one being launched) grants the invoker the authorization to run the atomic service in an embedded manner,the invoker can operate the atomic service in full-screen embedded mode. If authorization is not provided, the invoker will launch the atomic service in a pop-up manner.
    **NOTE**  
    
    To implement an embeddable atomic service within this component, it must inherit from  
    [EmbeddableUIAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. Otherwise, the system  
    cannot guarantee that the atomic service will function properly.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Component

<!--Device-unnamed-export declare struct FullScreenLaunchComponent--><!--Device-unnamed-export declare struct FullScreenLaunchComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## build

```TypeScript
build(): void
```

The method to build component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

<!--Device-FullScreenLaunchComponent-build(): void--><!--Device-FullScreenLaunchComponent-build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
content: ContentBuilder
```

Sets the component content.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @BuilderParam

<!--Device-FullScreenLaunchComponent-content: ContentBuilder--><!--Device-FullScreenLaunchComponent-content: ContentBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## appId

```TypeScript
appId: string
```

Indicates atomic service appId.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-FullScreenLaunchComponent-appId: string--><!--Device-FullScreenLaunchComponent-appId: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onError

```TypeScript
onError?: ErrorCallback
```

Callback triggered when an error occurs during running of the started ExtensionAbility.It is supported only when the atomic service runs in embedded mode,with the parameter being of type BusinessError.

**Type:** ErrorCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-FullScreenLaunchComponent-onError?: ErrorCallback--><!--Device-FullScreenLaunchComponent-onError?: ErrorCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onReceive

```TypeScript
onReceive?: Callback<Record<string, RecordData>>
```

Indicates the callback of onReceive.

**Type:** Callback&lt;Record&lt;string, RecordData&gt;&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-FullScreenLaunchComponent-onReceive?: Callback<Record<string, RecordData>>--><!--Device-FullScreenLaunchComponent-onReceive?: Callback<Record<string, RecordData>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTerminated

```TypeScript
onTerminated?: Callback<TerminationInfo>
```

Callback triggered when the EmbeddableUIAbility is terminated to receive the information about the termination. It is supported only when the atomic service runs in embedded mode,with the parameter being of type TerminationInfo.

**Type:** Callback&lt;TerminationInfo&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-FullScreenLaunchComponent-onTerminated?: Callback<TerminationInfo>--><!--Device-FullScreenLaunchComponent-onTerminated?: Callback<TerminationInfo>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
options?: AtomicServiceOptions
```

Indicates the atomic service start options.

**Type:** AtomicServiceOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-FullScreenLaunchComponent-options?: AtomicServiceOptions--><!--Device-FullScreenLaunchComponent-options?: AtomicServiceOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

