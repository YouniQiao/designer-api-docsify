# UIExtensionContext

UIExtensionContext provides the context environment for [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#uiextensionability). It inherits from [ExtensionContext](arkts-ability-extensioncontext-c.md#extensioncontext) and provides UIExtensionAbility-related configuration and APIs for operating the UIExtensionAbility. For example, you can use the APIs to start a UIExtensionAbility.

**Inheritance/Implementation:** UIExtensionContext extends ExtensionContext

**Since:** 23

<!--Device-unnamed-declare class UIExtensionContext--><!--Device-unnamed-declare class UIExtensionContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## connectServiceExtensionAbilityWithRootHostToken

```TypeScript
connectServiceExtensionAbilityWithRootHostToken(want: Want, connect: ConnectOptions): number
```

Connects the current UI extension to an service extension ability with a root host token. If the target service extension ability is visible, you can connect the target service extension ability; If the target service extension ability is invisible, you need to apply for permission:ohos.permission.START_INVISIBLE_ABILITY to connect target invisible service extension ability. If the target service extension ability is in cross-device, you need to apply for permission:ohos.permission.DISTRIBUTED_DATASYNC.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-connectServiceExtensionAbilityWithRootHostToken(want: Want, connect: ConnectOptions): long--><!--Device-UIExtensionContext-connectServiceExtensionAbilityWithRootHostToken(want: Want, connect: ConnectOptions): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| connect | [ConnectOptions](arkts-ability-connectoptions-connectoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000070](../errorcode-ability.md#16000070-extensionability-fails-to-start-a-serviceextensionability-in-strict-mode) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## setHostPageOverlayForbidden

```TypeScript
setHostPageOverlayForbidden(isForbidden: boolean) : void
```

Sets whether the page started by the [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#uiextensionability) can be overlaid by the page of the user. > **NOTE：**> > For details about the startup rules for the components in the stage model, see > [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md). > > This API must be called before a window is created. You are advised to call it within the > [onCreate](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#oncreate) lifecycle of the > [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#uiextensionability).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-setHostPageOverlayForbidden(isForbidden: boolean) : void--><!--Device-UIExtensionContext-setHostPageOverlayForbidden(isForbidden: boolean) : void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isForbidden | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## startAbilityForResultAsCaller

```TypeScript
startAbilityForResultAsCaller(want: Want, options?: StartOptions): Promise<AbilityResult>
```

Starts an ability with the caller information specified. The caller information is carried in **want** and identified at the system service layer. The ability can obtain the caller information from the **want** parameter in the **onCreate** lifecycle callback. When this API is used to start an ability, the caller information carried in **want** is not overwritten by the current application information. The system service layer can obtain the initial caller information. This API uses a promise to return the result. - Normally, you can call [terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) to terminate the ability. The result is returned to the caller. - If an exception occurs, for example, the ability is killed, an error message, in which **resultCode** is **-1**, is returned to the caller. - If different applications call this API to start an ability that uses the singleton mode and then call [terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) to terminate the ability, the normal result is returned to the last caller, and an exception message, in which **resultCode** is **-1**, is returned to others. > **NOTE：**> > For details about the startup rules for the components in the stage model, see > [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startAbilityForResultAsCaller(want: Want, options?: StartOptions): Promise<AbilityResult>--><!--Device-UIExtensionContext-startAbilityForResultAsCaller(want: Want, options?: StartOptions): Promise<AbilityResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000080](../errorcode-ability.md#16000080-new-instances-cannot-be-created) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000069](../errorcode-ability.md#16000069-extensionability-fails-to-start-a-thirdparty-application-in-strict-mode) |
| [16000070](../errorcode-ability.md#16000070-extensionability-fails-to-start-a-serviceextensionability-in-strict-mode) |
| [16000071](../errorcode-ability.md#16000071-application-clone-is-not-supported) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000076](../errorcode-ability.md#16000076-appinstancekey-does-not-exist) |
| [16000077](../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) |
| [16000078](../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) |
| [16000079](../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) |
| [16000072](../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) |
| [16000073](../errorcode-ability.md#16000073-appcloneindex-is-invalid) |

## startServiceExtensionAbility

```TypeScript
startServiceExtensionAbility(want: Want): Promise<void>
```

Starts a ServiceExtensionAbility. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startServiceExtensionAbility(want: Want): Promise<void>--><!--Device-UIExtensionContext-startServiceExtensionAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000019](../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## startServiceExtensionAbilityWithAccount

```TypeScript
startServiceExtensionAbilityWithAccount(want: Want, accountId: number): Promise<void>
```

Starts a ServiceExtensionAbility under a specified system account. This API uses a promise to return the result. > **NOTE：**> > For details about the startup rules for the components in the stage model, see > [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md). > > Permission verification is not required when **accountId** specifies the current user.

**Since:** 23

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>--><!--Device-UIExtensionContext-startServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| accountId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000019](../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## startUIAbilities

```TypeScript
startUIAbilities(wantList: Array<Want>): Promise<void>
```

Starts multiple UIAbility components simultaneously. This API uses a promise to return the result. You can pass the Want information of multiple UIAbility instances, which can point to one or more applications. If all the UIAbility instances can be started successfully, the system displays these UIAbility instances in multiple windows simultaneously. Depending on the window handling, different devices may have varying display effects ( including window shape, quantity, and layout). This API can be properly called only on phones and tablets. If it is called on other device types, error code 801 is returned. > **NOTE：**> > For details about the startup rules for the components in the stage model, see > [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startUIAbilities(wantList: Array<Want>): Promise<void>--><!--Device-UIExtensionContext-startUIAbilities(wantList: Array<Want>): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wantList | Array&lt;[Want](arkts-ability-app-ability-want-want-c.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16000080](../errorcode-ability.md#16000080-new-instances-cannot-be-created) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000124](../errorcode-ability.md#16000124-starting-a-distributed-uiability-is-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000125](../errorcode-ability.md#16000125-starting-a-plugin-is-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000126](../errorcode-ability.md#16000126-dlp-files-cannot-be-started) |
| [16000120](../errorcode-ability.md#16000120-number-of-elements-in-wantlist-exceeds-4-or-is-less-than-1) |
| [16000121](../errorcode-ability.md#16000121-target-component-is-not-a-uiability) |
| [16000122](../errorcode-ability.md#16000122-target-component-is-intercepted-by-the-system-control-module) |
| [16000123](../errorcode-ability.md#16000123-implicit-startup-is-not-supported) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16000076](../errorcode-ability.md#16000076-appinstancekey-does-not-exist) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000073](../errorcode-ability.md#16000073-appcloneindex-is-invalid) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## startUIAbilitiesInSplitWindowMode

```TypeScript
startUIAbilitiesInSplitWindowMode(primaryWindowId: number, secondaryWant: Want): Promise<void>
```

Starts a second UIAbility after the first UIAbility instance is created, and displays them in split-screen mode. This API uses a promise to return the result. This API can be properly called only on phones. If it is called on other device types, error code 801 is returned. > **NOTE：**> > If the first UIAbility instance is destroyed, the second UIAbility is started in full-screen mode. > > The second UIAbility supports only > [explicit startup](../../../application-models/explicit-implicit-want-mappings.md#matching-rules-of-explicit-want) > . > > If the caller is running in the background, the ohos.permission.START_ABILITIES_FROM_BACKGROUND permission is > required (available only for system applications). > > For details about the startup rules for the components in the stage model, see > [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 23

**Required permissions:** ohos.permission.START_ABILITIES_FROM_BACKGROUND

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startUIAbilitiesInSplitWindowMode(primaryWindowId: int, secondaryWant: Want): Promise<void>--><!--Device-UIExtensionContext-startUIAbilitiesInSplitWindowMode(primaryWindowId: int, secondaryWant: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| primaryWindowId | number | Yes |
| secondaryWant | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16000080](../errorcode-ability.md#16000080-new-instances-cannot-be-created) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000124](../errorcode-ability.md#16000124-starting-a-distributed-uiability-is-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000125](../errorcode-ability.md#16000125-starting-a-plugin-is-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000126](../errorcode-ability.md#16000126-dlp-files-cannot-be-started) |
| [16000122](../errorcode-ability.md#16000122-target-component-is-intercepted-by-the-system-control-module) |
| [16000123](../errorcode-ability.md#16000123-implicit-startup-is-not-supported) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000076](../errorcode-ability.md#16000076-appinstancekey-does-not-exist) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000073](../errorcode-ability.md#16000073-appcloneindex-is-invalid) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |
