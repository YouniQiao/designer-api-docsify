# Effect

Effect resource.

**Inheritance/Implementation:** Effect extends [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md#SceneResource)

**Since:** 21

<!--Device-unnamed-export interface Effect extends SceneResource--><!--Device-unnamed-export interface Effect extends SceneResource-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## getPropertyValue

```TypeScript
getPropertyValue(propertyName: string): Object | null | undefined
```

Get the value of a specific effect property.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Effect-getPropertyValue(propertyName: string): Object | null | undefined--><!--Device-Effect-getPropertyValue(propertyName: string): Object | null | undefined-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propertyName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Object |

## Examples

```TypeScript
import { SceneResourceFactory, Scene, Effect, EffectParameters } from '@kit.ArkGraphics3D';

function getEffectProperty() {
  let scene: Promise<Scene> = Scene.load();
  scene.then(async (result: Scene | undefined) => {
    if (!result) {
      return;
    }
    let sceneFactory: SceneResourceFactory = result.getResourceFactory();
    // Effect ID, which is in the format of 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX', for example, 'e68a7f45-2d21-4a0d-9aef-7d9c825d3f12'.
    let params: EffectParameters = {effectId: "e68a7f45-2d21-4a0d-9aef-7d9c825d3f12"};
    let effect: Effect = await sceneFactory.createEffect(params);
    effect.getPropertyValue('exposure');
  });
}
```

## setPropertyValue

```TypeScript
setPropertyValue(propertyName: string, value: Object | undefined): boolean
```

Set the value of a specific effect property

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Effect-setPropertyValue(propertyName: string, value: Object | undefined): boolean--><!--Device-Effect-setPropertyValue(propertyName: string, value: Object | undefined): boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propertyName | string | Yes |
| value | Object \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { SceneResourceFactory, Scene, Effect, EffectParameters } from '@kit.ArkGraphics3D';

function setEffectProperty() {
  let scene: Promise<Scene> = Scene.load();
  scene.then(async (result: Scene | undefined) => {
    if (!result) {
      return;
    }
    let sceneFactory: SceneResourceFactory = result.getResourceFactory();
    // Effect ID, which is in the format of 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX', for example, 'e68a7f45-2d21-4a0d-9aef-7d9c825d3f12'.
    let params: EffectParameters = {effectId: "e68a7f45-2d21-4a0d-9aef-7d9c825d3f12"};
    let effect: Effect = await sceneFactory.createEffect(params);
    effect.setPropertyValue('exposure', 1);
  });
}
```

## effectId

```TypeScript
readonly effectId: string
```

The id of the effect.This is the id that was used to create the effect.

**Type:** string

**Since:** 21

<!--Device-Effect-readonly effectId: string--><!--Device-Effect-readonly effectId: string-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## enabled

```TypeScript
enabled: boolean
```

Controls whether the effect is enabled or not.

**Type:** boolean

**Since:** 21

<!--Device-Effect-enabled: boolean--><!--Device-Effect-enabled: boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D
