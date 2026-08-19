# @ohos.arkui.advanced.InnerFullScreenLaunchComponent

## Modules to Import

```TypeScript
import { InnerFullScreenLaunchComponent, LaunchController } from '@kit.ArkUI';
```

## Summary

<!--Del-->
### Classes(System API)

| Name | Description |
| --- | --- |
| [LaunchController](arkts-arkui-arkui-advanced-innerfullscreenlaunchcomponent-launchcontroller-c-sys.md) | Controller for launching the atomic service. |
<!--DelEnd-->

<!--Del-->
### Structs(System API)

| Name | Description |
| --- | --- |
| [InnerFullScreenLaunchComponent](arkts-arkui-arkui-advanced-innerfullscreenlaunchcomponent-innerfullscreenlaunchcomponent-s-sys.md) | **InnerFullScreenLaunchComponent** is a component that allows the invoker to choose the timing for launching an atomic service. If the invoked app (the one being launched) grants the invoker the authorization to run the atomic service in an embedded manner, the invoker can operate the atomic service in full-screen embedded mode. If authorization is not provided, the invoker will launch the atomic service in a pop-up manner. &gt; **NOTE：**&gt; &gt; To implement an embeddable atomic service within this component, it must inherit from &gt; [EmbeddableUIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-embeddableuiability-embeddableuiability-c.md). If it does not inherit from &gt; **EmbeddableUIAbility**, the system cannot guarantee that the atomic service will function properly. |
<!--DelEnd-->

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [LaunchAtomicServiceCallback](arkts-arkui-launchatomicservicecallback-t-sys.md) | Triggered when an atomic service is launched. |
<!--DelEnd-->

