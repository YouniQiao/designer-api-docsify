# InnerFullScreenLaunchComponent (System API)

非显式全屏拉起原子化服务组件，拉起方可以选择拉起原子化服务的时机。当被拉起方授权使用方嵌入式运行原子化服务时，使用方全屏嵌入式运行原子化服务；未授权时，使用方跳出式拉起原子化服务。

> **说明：**
> 
> 该组件从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
> 
> 当需要在该组件中实现一个可嵌入式运行的原子化服务时，必须继承自
> [EmbeddableUIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-embeddableuiability-embeddableuiability-c.md/arkts-ability-app-ability-embeddableuiability-embeddableuiability-c.md)。若不继承自EmbeddableUIAbility，系统无
> 法保证原子化服务功能正常。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @Component

<!--Device-unnamed-export declare struct InnerFullScreenLaunchComponent--><!--Device-unnamed-export declare struct InnerFullScreenLaunchComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { InnerFullScreenLaunchComponent, LaunchController } from 'kits/@kit.ArkUI';
```

## content

```TypeScript
content: Callback<void>
```

组件显示内容。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @BuilderParam

<!--Device-InnerFullScreenLaunchComponent-content: Callback<void>--><!--Device-InnerFullScreenLaunchComponent-content: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## controller

```TypeScript
controller: LaunchController
```

拉起原子化服务的控制器。

**Type:** [LaunchController](arkts-arkui-arkui-advanced-innerfullscreenlaunchcomponent-launchcontroller-c-sys.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-InnerFullScreenLaunchComponent-controller: LaunchController--><!--Device-InnerFullScreenLaunchComponent-controller: LaunchController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## onError

```TypeScript
onError?: ErrorCallback
```

被拉起的嵌入式运行原子化服务在运行过程中发生异常时触发本回调。可通过回调参数中的code、name和message获取错误信息并做处理。

**Type:** [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-InnerFullScreenLaunchComponent-onError?: ErrorCallback--><!--Device-InnerFullScreenLaunchComponent-onError?: ErrorCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## onReceive

```TypeScript
onReceive?: Callback<Record<string, Object>>
```

被拉起的嵌入式运行原子化服务通过[@ohos.window (窗口)](arkts-window.md)调用相关API时，触发本回调。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-InnerFullScreenLaunchComponent-onReceive?: Callback<Record<string, Object>>--><!--Device-InnerFullScreenLaunchComponent-onReceive?: Callback<Record<string, Object>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## onTerminated

```TypeScript
onTerminated?: Callback<TerminationInfo>
```

被拉起的嵌入式运行原子化服务通过点击原子化服务退出按钮、手势侧滑、调用  
[terminateSelfWithResult](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md/arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)或者  
[terminateSelf](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md/arkts-ability-uiabilitycontext-c.md#terminateself)正常退出时，触发本回调。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TerminationInfo&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-InnerFullScreenLaunchComponent-onTerminated?: Callback<TerminationInfo>--><!--Device-InnerFullScreenLaunchComponent-onTerminated?: Callback<TerminationInfo>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

