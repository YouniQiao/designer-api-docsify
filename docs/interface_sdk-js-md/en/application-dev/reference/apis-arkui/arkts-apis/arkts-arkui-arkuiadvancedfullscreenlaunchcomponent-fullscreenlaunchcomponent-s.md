# FullScreenLaunchComponent

*FullScreenLaunchComponent** is a component designed for launching atomic services in full screen. If the invoked app (the one being launched) grants the invoker the authorization to run the atomic service in an embedded manner, the invoker can operate the atomic service in full-screen embedded mode. If authorization is not provided, the invoker will launch the atomic service in a pop-up manner.

> **NOTE：**
> 
> To implement an embeddable atomic service within this component, it must inherit from
> [EmbeddableUIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-appabilityembeddableuiability-embeddableuiability-c.md). Otherwise, the system
> cannot guarantee that the atomic service will function properly.

@struct { FullScreenLaunchComponent }

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare struct FullScreenLaunchComponent--><!--Device-unnamed-export declare struct FullScreenLaunchComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { FullScreenLaunchComponent } from '@kit.ArkUI';
```

## build

```TypeScript
@Builder
  build(): void
```

The method to build component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-FullScreenLaunchComponent-@Builder  build(): void--><!--Device-FullScreenLaunchComponent-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## appId

```TypeScript
appId: string
```

Indicates atomic service appId.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-FullScreenLaunchComponent-appId: string--><!--Device-FullScreenLaunchComponent-appId: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
@BuilderParam
  content: ContentBuilder
```

Sets the component content.

**Type:** [ContentBuilder](arkts-arkui-contentbuilder-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-FullScreenLaunchComponent-@BuilderParam  content: ContentBuilder--><!--Device-FullScreenLaunchComponent-@BuilderParam  content: ContentBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onError

```TypeScript
onError?: ErrorCallback
```

Callback triggered when an error occurs during running of the started ExtensionAbility. It is supported only when the atomic service runs in embedded mode, with the parameter being of type BusinessError.

**Type:** [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-errorcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-FullScreenLaunchComponent-onError?: ErrorCallback--><!--Device-FullScreenLaunchComponent-onError?: ErrorCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onReceive

```TypeScript
onReceive?: Callback<Record<string, RecordData>>
```

Indicates the callback of onReceive.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt;&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-FullScreenLaunchComponent-onReceive?: Callback<Record<string, RecordData>>--><!--Device-FullScreenLaunchComponent-onReceive?: Callback<Record<string, RecordData>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTerminated

```TypeScript
onTerminated?: Callback<TerminationInfo>
```

Callback triggered when the EmbeddableUIAbility is terminated to receive the information about the termination. It is supported only when the atomic service runs in embedded mode, with the parameter being of type TerminationInfo.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;TerminationInfo&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-FullScreenLaunchComponent-onTerminated?: Callback<TerminationInfo>--><!--Device-FullScreenLaunchComponent-onTerminated?: Callback<TerminationInfo>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
options?: AtomicServiceOptions
```

Indicates the atomic service start options.

**Type:** [AtomicServiceOptions](../../apis-ability-kit/arkts-apis/arkts-ability-appabilityatomicserviceoptions-atomicserviceoptions-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-FullScreenLaunchComponent-options?: AtomicServiceOptions--><!--Device-FullScreenLaunchComponent-options?: AtomicServiceOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

