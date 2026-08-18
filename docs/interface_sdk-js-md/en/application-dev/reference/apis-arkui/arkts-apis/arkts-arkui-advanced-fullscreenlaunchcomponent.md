# @ohos.arkui.advanced.FullScreenLaunchComponent

## Modules to Import

```TypeScript
import { FullScreenLaunchComponent } from '@kit.ArkUI';
```

## Summary

### Structs

| Name | Description |
| --- | --- |
| [FullScreenLaunchComponent](arkts-arkui-arkui-advanced-fullscreenlaunchcomponent-fullscreenlaunchcomponent-s.md) | **FullScreenLaunchComponent** is a component designed for launching atomic services in full screen. If the invoked app (the one being launched) grants the invoker the authorization to run the atomic service in an embedded manner, the invoker can operate the atomic service in full-screen embedded mode. If authorization is not provided, the invoker will launch the atomic service in a pop-up manner. > **NOTE：**> > To implement an embeddable atomic service within this component, it must inherit from > [EmbeddableUIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-embeddableuiability-embeddableuiability-c.md#embeddableuiability). Otherwise, the system > cannot guarantee that the atomic service will function properly. |

### Types

| Name | Description |
| --- | --- |
| [ContentBuilder](arkts-arkui-contentbuilder-t.md) | Defines ContentBuilder. |

