# PhotoEditorExtensionAbility

Class of the photo editor ExtensionAbility, which provides APIs for you to edit photos.

**继承/实现关系：** PhotoEditorExtensionAbility extends [ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare class PhotoEditorExtensionAbility extends ExtensionAbility--><!--Device-unnamed-declare class PhotoEditorExtensionAbility extends ExtensionAbility-End-->

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

## 导入模块

```TypeScript
import { PhotoEditorExtensionAbility } from 'kits/@kit.AbilityKit';
```

## onBackground

```TypeScript
onBackground(): void
```

Called back when the state of an UI extension changes to background.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoEditorExtensionAbility-onBackground(): void--><!--Device-PhotoEditorExtensionAbility-onBackground(): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## 示例

```TypeScript
import { PhotoEditorExtensionAbility } from '@kit.AbilityKit';

const TAG: string = '[testTag] ExamplePhotoEditorAbility';

export default class ExamplePhotoEditorAbility extends PhotoEditorExtensionAbility {
  onBackground() {
    console.info(TAG, `onBackground`);
  }
}
```

## onCreate

```TypeScript
onCreate(): void
```

Called back when an UI extension is started for initialization.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoEditorExtensionAbility-onCreate(): void--><!--Device-PhotoEditorExtensionAbility-onCreate(): void-End-->

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

## 示例

```TypeScript
import { PhotoEditorExtensionAbility } from '@kit.AbilityKit';

const TAG: string = '[testTag] ExamplePhotoEditorAbility';

export default class ExamplePhotoEditorAbility extends PhotoEditorExtensionAbility {
  onCreate() {
    console.info(TAG, `onCreate`);
  }
}
```

## onDestroy

```TypeScript
onDestroy(): void | Promise<void>
```

Called back before an UI extension is destroyed.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoEditorExtensionAbility-onDestroy(): void | Promise<void>--><!--Device-PhotoEditorExtensionAbility-onDestroy(): void | Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

## 示例

同步回调示例如下：

```TypeScript
import { PhotoEditorExtensionAbility } from '@kit.AbilityKit';

const TAG: string = '[testTag] ExamplePhotoEditorAbility';

export default class ExamplePhotoEditorAbility extends PhotoEditorExtensionAbility {
  onDestroy() {
    console.info(TAG, `onDestroy`);
    // 调用同步函数...
  }
}
```

Promise异步回调示例如下：

```TypeScript
import { PhotoEditorExtensionAbility } from '@kit.AbilityKit';

const TAG: string = '[testTag] ExamplePhotoEditorAbility';

export default class ExamplePhotoEditorAbility extends PhotoEditorExtensionAbility {
  async onDestroy() {
    console.info(TAG, `onDestroy`);
    // 调用异步函数...
  }
}
```

## onDestroy

```TypeScript
onDestroy(): Promise<void> | undefined
```

Called back before an UI extension is destroyed.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoEditorExtensionAbility-onDestroy(): Promise<void> | undefined--><!--Device-PhotoEditorExtensionAbility-onDestroy(): Promise<void> | undefined-End-->

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

## onForeground

```TypeScript
onForeground(): void
```

Called back when the state of an UI extension changes to foreground.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoEditorExtensionAbility-onForeground(): void--><!--Device-PhotoEditorExtensionAbility-onForeground(): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## 示例

```TypeScript
import { PhotoEditorExtensionAbility } from '@kit.AbilityKit';

const TAG: string = '[testTag] ExamplePhotoEditorAbility';

export default class ExamplePhotoEditorAbility extends PhotoEditorExtensionAbility {
  onForeground() {
    console.info(TAG, `onForeground`);
  }
}
```

## onStartContentEditing

```TypeScript
onStartContentEditing(uri: string, want: Want, session: UIExtensionContentSession): void
```

Called back when an UI extension session is created and original image is ready.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoEditorExtensionAbility-onStartContentEditing(uri: string, want: Want, session: UIExtensionContentSession): void--><!--Device-PhotoEditorExtensionAbility-onStartContentEditing(uri: string, want: Want, session: UIExtensionContentSession): void-End-->

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | Indicates the uri info of the original image. |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 | Indicates the want info of the UI extension. |
| session | [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md) | 是 | Indicates the session of the UI extension page. |

## 示例

```TypeScript
import { PhotoEditorExtensionAbility, Want, UIExtensionContentSession } from '@kit.AbilityKit';

const TAG: string = '[testTag] ExamplePhotoEditorAbility';

export default class ExamplePhotoEditorAbility extends PhotoEditorExtensionAbility {
  onStartContentEditing(uri: string, want: Want, session: UIExtensionContentSession) {
    console.info(TAG, `onStartContentEditing want: ${JSON.stringify(want)}, uri: ${uri}`);
  }
}
```

## context

```TypeScript
context: PhotoEditorExtensionContext
```

Indicates configuration information about an Photo editor extension ability context.

**类型：** [PhotoEditorExtensionContext](arkts-ability-photoeditorextensioncontext-c.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoEditorExtensionAbility-context: PhotoEditorExtensionContext--><!--Device-PhotoEditorExtensionAbility-context: PhotoEditorExtensionContext-End-->

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

