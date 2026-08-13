# @ohos.app.ability.contextConstant

/*
 Copyright (c) 2022-2024 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace contextConstant--><!--Device-unnamed-declare namespace contextConstant-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { contextConstant } from '@kit.AbilityKit';
```

## Summary

### Enums

| Name | Description |
| --- | --- |
| [AreaMode](arkts-ability-contextconstant-areamode-e.md) | Enumerates the file encryption levels, which are used to ensure data security for applications across different scenarios. You can select the appropriate encryption level based on the application requirements to protect user data. |
| [ContextType](arkts-ability-contextconstant-contexttype-e.md) | Context type |
| [ProcessMode](arkts-ability-contextconstant-processmode-e.md) | Enumerates the process modes of the UIAbility after it is started. As a property of [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md#StartOptions), **ProcessMode** takes effect only in [UIAbilityContext.startAbility](arkts-ability-uiabilitycontext-c.md#startAbility) and is used to specify the process mode of the target UIAbility. This value takes effect only on 2-in-1 devices and tablets. If it is used on other devices, error code 801 is returned. |
| [Scenarios](arkts-ability-contextconstant-scenarios-e.md) | Enumerates the scenarios where the [onNewWant](arkts-ability-app-ability-uiability-uiability-c.md#onNewWant) lifecycle callback is not triggered. It is used in the [setOnNewWantSkipScenarios](arkts-ability-uiabilitycontext-c.md#setOnNewWantSkipScenarios) API. |
| [StartupVisibility](arkts-ability-contextconstant-startupvisibility-e.md) | Enumerates the visibility statuses of the UIAbility after it is started. If the target UIAbility is set to invisible, the window of the target UIAbility is not displayed in the foreground, there is no icon in the dock, and the **onForeground** lifecycle of the target UIAbility is not triggered. As a property of [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md#StartOptions), **StartupVisibility** takes effect only in [UIAbilityContext.startAbility](arkts-ability-uiabilitycontext-c.md#startAbility) and specifies the visibility of the target UIAbility after it is started. This value takes effect only on 2-in-1 devices and tablets. If it is used on other devices, error code 801 is returned. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [ContextType](arkts-ability-contextconstant-contexttype-e-sys.md) | Context type |
<!--DelEnd-->

