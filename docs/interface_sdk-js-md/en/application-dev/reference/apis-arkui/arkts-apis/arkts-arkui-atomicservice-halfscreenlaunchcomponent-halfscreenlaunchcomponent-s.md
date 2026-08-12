# HalfScreenLaunchComponent

**HalfScreenLaunchComponent** is a component designed for launching atomic services in half screen. If the invoked application (the one being launched) grants the invoker the authorization to run the atomic service in an embedded manner, the invoker can operate the atomic service in half-screen embedded mode. If authorization is not provided,the invoker will launch the atomic service in a pop-up manner.

> **NOTE：**
> 
> To implement an embeddable atomic service, make sure it inherits from
> [EmbeddableUIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-embeddableuiability-embeddableuiability-c.md#EmbeddableUIAbility). If the atomic service does
> not inherit from **EmbeddableUIAbility**, the system cannot guarantee its proper operation.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Decorator:** @Component

<!--Device-unnamed-export declare struct HalfScreenLaunchComponent--><!--Device-unnamed-export declare struct HalfScreenLaunchComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { HalfScreenLaunchComponent } from '@kit.ArkUI';
```

## appId

```TypeScript
appId: string
```

Application ID for the atomic service.

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-HalfScreenLaunchComponent-appId: string--><!--Device-HalfScreenLaunchComponent-appId: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
content: Callback<void>
```

Content displayed in the component.

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Decorator:** @BuilderParam

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-HalfScreenLaunchComponent-content: Callback<void>--><!--Device-HalfScreenLaunchComponent-content: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onError

```TypeScript
onError?: ErrorCallback
```

Invoked when an error occurs during the running of the atomic service.

**Type:** [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-errorcallback-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-HalfScreenLaunchComponent-onError?: ErrorCallback--><!--Device-HalfScreenLaunchComponent-onError?: ErrorCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onReceive

```TypeScript
onReceive?: Callback<Record<string, Object>>
```

Callback triggered when an embedded atomic service calls [@ohos.window (window)](@ohos.window) APIs.

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Record&lt;string, Object&gt;&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-HalfScreenLaunchComponent-onReceive?: Callback<Record<string, Object>>--><!--Device-HalfScreenLaunchComponent-onReceive?: Callback<Record<string, Object>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTerminated

```TypeScript
onTerminated?: Callback<TerminationInfo>
```

Callback triggered when an embedded atomic service exits normally. Exit scenarios include user-triggered exit button taps or edge swipes, or calls to  
[terminateSelfWithResult](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md#terminateSelfWithResult)or  
[terminateSelf](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md#terminateSelf).

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;TerminationInfo&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-HalfScreenLaunchComponent-onTerminated?: Callback<TerminationInfo>--><!--Device-HalfScreenLaunchComponent-onTerminated?: Callback<TerminationInfo>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
options?: AtomicServiceOptions
```

Parameters for starting the atomic service. The default value is empty.

**Type:** [AtomicServiceOptions](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-atomicserviceoptions-atomicserviceoptions-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-HalfScreenLaunchComponent-options?: AtomicServiceOptions--><!--Device-HalfScreenLaunchComponent-options?: AtomicServiceOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

