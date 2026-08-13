# startAbility

## Modules to Import

```TypeScript
import { featureAbility } from '@kit.AbilityKit';
```

## startAbility

```TypeScript
function startAbility(parameter: StartAbilityParameter, callback: AsyncCallback<number>): void
```

Starts an ability. This API uses an asynchronous callback to return the result. > **NOTE：**> > For details about the startup rules for the components in the FA model, see > [Component Startup Rules (FA Model)](../../../application-models/component-startup-rules-fa.md).

**Since:** 6

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-featureAbility-function startAbility(parameter: StartAbilityParameter, callback: AsyncCallback<number>): void--><!--Device-featureAbility-function startAbility(parameter: StartAbilityParameter, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parameter | [StartAbilityParameter](arkts-ability-startabilityparameter-startabilityparameter-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## Examples

```TypeScript
import { featureAbility, wantConstant } from '@kit.AbilityKit';

featureAbility.startAbility(
  {
    want:
    {
      action: '',
      entities: [''],
      type: '',
      flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.myapplication',
      /* In the FA model, abilityName consists of package and ability names. */
      abilityName: 'com.example.myapplication.secondAbility',
      uri: ''
    },
  },
  (error, data) => {
    if (error && error.code !== 0) {
      console.error(`startAbility fail, error: ${JSON.stringify(error)}`);
    } else {
      console.info(`startAbility success, data: ${JSON.stringify(data)}`);
    }
  }
);
```


## startAbility

```TypeScript
function startAbility(parameter: StartAbilityParameter): Promise<number>
```

Starts an ability. This API uses a promise to return the result. > **NOTE：**> > For details about the startup rules for the components in the FA model, see > [Component Startup Rules (FA Model)](../../../application-models/component-startup-rules-fa.md).

**Since:** 6

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-featureAbility-function startAbility(parameter: StartAbilityParameter): Promise<number>--><!--Device-featureAbility-function startAbility(parameter: StartAbilityParameter): Promise<number>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parameter | [StartAbilityParameter](arkts-ability-startabilityparameter-startabilityparameter-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## Examples

```TypeScript
import { featureAbility, wantConstant } from '@kit.AbilityKit';

featureAbility.startAbility(
  {
    want:
    {
      action: 'ohos.want.action.home',
      entities: ['entity.system.home'],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.myapplication',
      /* In the FA model, abilityName consists of package and ability names. */
      abilityName: 'com.example.myapplication.secondAbility',
      uri: ''
    },
  }
).then((data) => {
  console.info(`startAbility data: ${JSON.stringify(data)}`);
});
```
