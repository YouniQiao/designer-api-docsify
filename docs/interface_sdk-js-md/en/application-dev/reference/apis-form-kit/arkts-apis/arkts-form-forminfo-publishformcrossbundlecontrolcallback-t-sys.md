# PublishFormCrossBundleControlCallback (System API)

```TypeScript
type PublishFormCrossBundleControlCallback = (info: PublishFormCrossBundleInfo) => boolean
```

publish form cross bundle control callback.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [PublishFormCrossBundleInfo](arkts-form-forminfo-publishformcrossbundleinfo-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
import { formInfo } from '@kit.FormKit';

let publishFormCrossBundleControlCallback: formInfo.PublishFormCrossBundleControlCallback =
  (info: formInfo.PublishFormCrossBundleInfo): boolean => {
    console.info('publish form cross bundle info callback success.');
    return true;
  };
```
