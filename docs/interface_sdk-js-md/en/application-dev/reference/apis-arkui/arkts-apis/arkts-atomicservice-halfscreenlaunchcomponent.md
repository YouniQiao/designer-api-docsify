# @ohos.atomicservice.HalfScreenLaunchComponent

## Modules to Import

```TypeScript
import { HalfScreenLaunchComponent } from '@kit.ArkUI';
```

## Summary

### Structs

| Name | Description |
| --- | --- |
| [HalfScreenLaunchComponent](arkts-arkui-atomicservice-halfscreenlaunchcomponent-halfscreenlaunchcomponent-s.md) | **HalfScreenLaunchComponent** is a component designed for launching atomic services in half screen. If the invoked application (the one being launched) grants the invoker the authorization to run the atomic service in an embedded manner, the invoker can operate the atomic service in half-screen embedded mode. If authorization is not provided, the invoker will launch the atomic service in a pop-up manner. > **NOTE：**> > To implement an embeddable atomic service, make sure it inherits from > [EmbeddableUIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-embeddableuiability-embeddableuiability-c.md). If the atomic service does > not inherit from **EmbeddableUIAbility**, the system cannot guarantee its proper operation. |

