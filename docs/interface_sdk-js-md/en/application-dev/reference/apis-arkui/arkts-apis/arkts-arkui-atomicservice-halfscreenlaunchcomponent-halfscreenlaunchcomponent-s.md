# HalfScreenLaunchComponent

半屏嵌入式启动原子化服务组件，当被拉起方未授权嵌入式运行原子化服务时，宿主将使用跳出式拉起原子化服务。

> **说明：**
> 
> 该组件从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
> 
> 当需要在该组件中实现一个可嵌入式运行的原子化服务时，原子化服务必须继承自
> [EmbeddableUIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-embeddableuiability-embeddableuiability-c.md/arkts-ability-app-ability-embeddableuiability-embeddableuiability-c.md)。若不继承自EmbeddableUIAbility，系统无
> 法确保原子化服务正常运行。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Decorator:** @Component

<!--Device-unnamed-export declare struct HalfScreenLaunchComponent--><!--Device-unnamed-export declare struct HalfScreenLaunchComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { HalfScreenLaunchComponent } from 'kits/@kit.ArkUI';
```

## appId

```TypeScript
appId: string
```

原子化服务appId。

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

组件显示内容。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt;

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

被拉起的原子化服务在运行过程中发生异常时触发本回调。

**Type:** [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-HalfScreenLaunchComponent-onError?: ErrorCallback--><!--Device-HalfScreenLaunchComponent-onError?: ErrorCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onReceive

```TypeScript
onReceive?: Callback<Record<string, Object>>
```

被拉起的嵌入式运行原子化服务通过[@ohos.window (窗口)](arkts-window.md)调用相关API时，触发本回调。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-HalfScreenLaunchComponent-onReceive?: Callback<Record<string, Object>>--><!--Device-HalfScreenLaunchComponent-onReceive?: Callback<Record<string, Object>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTerminated

```TypeScript
onTerminated?: Callback<TerminationInfo>
```

被拉起的嵌入式运行原子化服务通过点击原子化服务退出按钮、手势侧滑、调用  
[terminateSelfWithResult](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md/arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)或者  
[terminateSelf](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md/arkts-ability-uiabilitycontext-c.md#terminateself)正常退出时，触发本回调。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TerminationInfo&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-HalfScreenLaunchComponent-onTerminated?: Callback<TerminationInfo>--><!--Device-HalfScreenLaunchComponent-onTerminated?: Callback<TerminationInfo>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
options?: AtomicServiceOptions
```

拉起原子化服务参数。不填时使用默认参数拉起原子化服务。

**Type:** [AtomicServiceOptions](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-atomicserviceoptions-atomicserviceoptions-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-HalfScreenLaunchComponent-options?: AtomicServiceOptions--><!--Device-HalfScreenLaunchComponent-options?: AtomicServiceOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

