# getAppPreloadType

## Modules to Import

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
```

## getAppPreloadType

```TypeScript
export function getAppPreloadType(): AppPreloadType
```

获取应用当前进程的预加载类型。

> **说明：**
> 
> - 只有在进程首次执行[AbilityStage.onCreate](arkts-ability-app-ability-abilitystage-abilitystage-c.md#oncreate)完成之前调用该接口，才可以返回真实的预
> 加载类型。
> 
> - AbilityStage创建完成后，应用的预加载数据将被清除，调用该接口将返回UNSPECIFIED，无法获取到真实的预加载类型。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-application-export function getAppPreloadType(): AppPreloadType--><!--Device-application-export function getAppPreloadType(): AppPreloadType-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| [AppPreloadType](arkts-ability-application-apppreloadtype-e.md) | 应用当前进程的预加载类型。 |

## Examples

```TypeScript
import { AbilityStage, application } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage{
  onCreate() {
    let appPreloadType = application.getAppPreloadType();
  }
}
```

