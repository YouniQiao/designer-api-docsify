# setDisposedRules (System API)

## Modules to Import

```TypeScript
import { appControl } from 'kits/@kit.AbilityKit';
```

## setDisposedRules

```TypeScript
function setDisposedRules(disposedRuleConfigurations: Array<DisposedRuleConfiguration>): void
```

批量设置指定应用或分身应用的拦截规则。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_DISPOSED_APP_STATUS

<!--Device-appControl-function setDisposedRules(disposedRuleConfigurations: Array<DisposedRuleConfiguration>): void--><!--Device-appControl-function setDisposedRules(disposedRuleConfigurations: Array<DisposedRuleConfiguration>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| disposedRuleConfigurations | Array&lt;DisposedRuleConfiguration&gt; | Yes | 表示批量设置拦截规则的配置，包括待拦截应用的appId、分身应用索引及拦截规则。每次 设置拦截规则的数组的最大数量为1000。&lt;br/&gt;**说明：**&lt;br/&gt;1.如果数组中存在appId和appIndex相同的DisposedRuleConfiguration时，后面的 DisposedRuleConfiguration会覆盖前面的。&lt;br/&gt;2.如果应用已设置过拦截规则，重新为该应用设置拦截规则，会覆盖之前的。appId和appIndex一致则表示同一应用。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 17700061 | AppIndex is not in the valid range. |
| 201 | Permission denied. |
| 202 | Permission denied. A non-system application is not allowed to call a system API. |
| 17700005 | The specified app ID is invalid. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { appControl, Want, bundleManager } from '@kit.AbilityKit';

let want: Want = {
  bundleName: 'com.example.myapplication',
  moduleName: 'entry',
  abilityName: 'EntryAbility'
};
let elementName: bundleManager.ElementName = {
  bundleName: 'com.example.myapplication',
  moduleName: 'entry',
  abilityName: 'EntryAbility'
};
let rule: appControl.DisposedRule = {
  want: want,
  componentType: appControl.ComponentType.UI_ABILITY,
  disposedType: appControl.DisposedType.BLOCK_APPLICATION,
  controlType: appControl.ControlType.ALLOWED_LIST,
  elementList: [
    elementName
  ],
  priority: 100
};

let disposedRuleConfiguration: appControl.DisposedRuleConfiguration = {
  appId: 'com.example.myapplication_BInGTMPMdc6v55s/UFIJHL5NLREXjOuxm/DsyMhlFmLAZC9/Gk+ruqS9OZr/dvFuaIaQQL1pKolvzK/zYNHvJ/I=',
  appIndex: 0,
  disposedRule: rule,
};

let disposedRuleConfigurations: Array<appControl.DisposedRuleConfiguration> = [];
disposedRuleConfigurations.push(disposedRuleConfiguration);

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('setDisposedRules', { type: ButtonType.Normal })
          .onClick(() => {
            try {
              appControl.setDisposedRules(disposedRuleConfigurations);
              console.info('setDisposedRules success');
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              console.error(`setDisposedRules failed, errCode:${err.code}, message:${err.message}`);
            }
          });
      }
    }
  }
}
```

