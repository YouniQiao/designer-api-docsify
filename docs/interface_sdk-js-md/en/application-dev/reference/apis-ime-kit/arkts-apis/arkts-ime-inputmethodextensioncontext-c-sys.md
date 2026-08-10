# InputMethodExtensionContext

**@ohos.InputMethodExtensionContext**模块是InputMethodExtensionAbility的上下文环境，继承于ExtensionContext，为输入法扩展能力提供上下文级别的操作接口。

本模块是输入法ExtensionAbility的上下文类，继承自`ExtensionContext`，作为`InputMethodExtensionAbility`实例的`context`属性提供。它承载了输入法扩展应用在其生命周期内可使用的上下文能力，包括销毁自身和拉起其他应用。

本模块提供两大核心能力：1）通过`destroy()`销毁输入法ExtensionAbility自身，实现输入法应用的生命周期终止；2）通过`startAbility()`拉起目标应用，使输入法应用能够启动其他Ability进行交互，拓展输入法功能的灵活性和可扩展性。

当开发输入法ExtensionAbility并需要在其生命周期内执行上下文级操作时使用本模块。典型场景包括：输入法应用在`onDestroy`回调中主动销毁自身、输入法应用需要拉起设置页面或其他辅助应用等。

模块内的核心API按功能分为两类：

1. **生命周期管理**：`destroy()`用于销毁输入法ExtensionAbility自身，终止输入法应用运行。2. **Ability交互**：`startAbility()`用于从输入法应用拉起目标Ability（如设置页面等），拓展输入法应用与其他应用的交互能力。

典型使用流程：在`InputMethodExtensionAbility`的`onCreate`回调中获取`this.context` → 在需要终止输入法时调用`context.destroy()` → 在需要拉起其他应用时调用`context.startAbility(want)`。

**Inheritance/Implementation:** InputMethodExtensionContext extends [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class InputMethodExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class InputMethodExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { InputMethodExtensionContext } from 'kits/@kit.IMEKit';
```

## connectAbility

```TypeScript
connectAbility(want: Want, options: ConnectOptions): number
```

将当前Ability连接到ServiceExtensionAbility。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodExtensionContext-connectAbility(want: Want, options: ConnectOptions): number--><!--Device-InputMethodExtensionContext-connectAbility(want: Want, options: ConnectOptions): number-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 用于指定目标ServiceExtensionAbility的Want类型信息。 |
| options | [ConnectOptions](../../apis-ability-kit/arkts-apis/arkts-ability-connectoptions-connectoptions-i.md) | Yes | 连接回调，用于返回连接成功、中断或失败的信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 连接的数字标识，用于后续断开连接时传入。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000004 | Cannot start an invisible component.<br>**Applicable version:** 10 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000005 | The specified process does not have the permission. |
| 16000053 | The ability is not on the top of the UI.<br>**Applicable version:** 10 and later |
| 16000006 | Cross-user operations are not allowed.<br>**Applicable version:** 10 and later |
| 16000055 | Installation-free timed out.<br>**Applicable version:** 10 and later |
| 16000001 | The specified ability does not exist. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed. 2. System service failed to communicate with dependency module. |
| 16000002 | Incorrect ability type.<br>**Applicable version:** 10 and later |
| 16000008 | The crowdtesting application expires.<br>**Applicable version:** 10 and later |
| 16000011 | The context does not exist. |

## connectAbilityWithAccount

```TypeScript
connectAbilityWithAccount(want: Want, accountId: number): number
```

以指定账户连接ServiceExtensionAbility。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodExtensionContext-connectAbilityWithAccount(want: Want, accountId: number): number--><!--Device-InputMethodExtensionContext-connectAbilityWithAccount(want: Want, accountId: number): number-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 用于指定目标ServiceExtensionAbility的Want类型信息。 |
| accountId | number | Yes | 目标系统账户的ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 连接的数字标识，用于后续断开连接时传入。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI.<br>**Applicable version:** 10 and later |
| 16000055 | Installation-free timed out.<br>**Applicable version:** 10 and later |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed. 2. System service failed to communicate with dependency module. |
| 201 | The application does not have permission to call the interface. |
| 202 | not system application. |
| 16000004 | Cannot start an invisible component.<br>**Applicable version:** 10 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed.<br>**Applicable version:** 10 and later |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type.<br>**Applicable version:** 10 and later |
| 16000008 | The crowdtesting application expires.<br>**Applicable version:** 10 and later |
| 16000011 | The context does not exist. |

## connectServiceExtensionAbility

```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
```

将当前Ability连接到ServiceExtensionAbility。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): number--><!--Device-InputMethodExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): number-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 用于指定目标ServiceExtensionAbility的Want类型信息。 |
| options | [ConnectOptions](../../apis-ability-kit/arkts-apis/arkts-ability-connectoptions-connectoptions-i.md) | Yes | 连接回调，用于返回连接成功、中断或失败的信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 连接的数字标识，用于后续断开连接时传入。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000004 | Cannot start an invisible component.<br>**Applicable version:** 10 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000005 | The specified process does not have the permission. |
| 16000053 | The ability is not on the top of the UI.<br>**Applicable version:** 10 and later |
| 16000006 | Cross-user operations are not allowed.<br>**Applicable version:** 10 and later |
| 16000055 | Installation-free timed out.<br>**Applicable version:** 10 and later |
| 16000001 | The specified ability does not exist. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed. 2. System service failed to communicate with dependency module. |
| 16000002 | Incorrect ability type.<br>**Applicable version:** 10 and later |
| 16000008 | The crowdtesting application expires.<br>**Applicable version:** 10 and later |
| 16000011 | The context does not exist. |

## disconnectAbility

```TypeScript
disconnectAbility(connection: number, callback: AsyncCallback<void>): void
```

断开与ServiceExtensionAbility的连接。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodExtensionContext-disconnectAbility(connection: number, callback: AsyncCallback<void>): void--><!--Device-InputMethodExtensionContext-disconnectAbility(connection: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connection | number | Yes | 连接的数字标识，由connectAbility/connectServiceExtensionAbility返回。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当断开连接成功时，err为undefined；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed. 2. System service failed to communicate with dependency module. |
| 16000011 | The context does not exist. |

## disconnectAbility

```TypeScript
disconnectAbility(connection: number): Promise<void>
```

断开与ServiceExtensionAbility的连接。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodExtensionContext-disconnectAbility(connection: number): Promise<void>--><!--Device-InputMethodExtensionContext-disconnectAbility(connection: number): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connection | number | Yes | 连接的数字标识，由connectAbility/connectServiceExtensionAbility返回。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed. 2. System service failed to communicate with dependency module. |
| 16000011 | The context does not exist. |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number, callback: AsyncCallback<void>): void
```

断开与ServiceExtensionAbility的连接。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodExtensionContext-disconnectServiceExtensionAbility(connection: number, callback: AsyncCallback<void>): void--><!--Device-InputMethodExtensionContext-disconnectServiceExtensionAbility(connection: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connection | number | Yes | 连接的数字标识，由connectServiceExtensionAbility返回。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当断开连接成功时，err为undefined；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed. 2. System service failed to communicate with dependency module. |
| 16000011 | The context does not exist. |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number): Promise<void>
```

断开与ServiceExtensionAbility的连接。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodExtensionContext-disconnectServiceExtensionAbility(connection: number): Promise<void>--><!--Device-InputMethodExtensionContext-disconnectServiceExtensionAbility(connection: number): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connection | number | Yes | 连接的数字标识，由connectServiceExtensionAbility返回。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed. 2. System service failed to communicate with dependency module. |
| 16000011 | The context does not exist. |

## startAbilityWithAccount

```TypeScript
startAbilityWithAccount(want: Want, accountId: number, callback: AsyncCallback<void>): void
```

以指定账户拉起目标应用。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodExtensionContext-startAbilityWithAccount(want: Want, accountId: number, callback: AsyncCallback<void>): void--><!--Device-InputMethodExtensionContext-startAbilityWithAccount(want: Want, accountId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 用于指定目标应用的Want类型信息。 |
| accountId | number | Yes | 目标系统账户的ID。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当拉起目标应用成功时，err为undefined；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed. 2. System service failed to communicate with dependency module. |
| 201 | The application does not have permission to call the interface. |
| 202 | not system application. |
| 16000004 | Cannot start an invisible component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |

## startAbilityWithAccount

```TypeScript
startAbilityWithAccount(want: Want, accountId: number): Promise<void>
```

以指定账户拉起目标应用。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodExtensionContext-startAbilityWithAccount(want: Want, accountId: number): Promise<void>--><!--Device-InputMethodExtensionContext-startAbilityWithAccount(want: Want, accountId: number): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 用于指定目标应用的Want类型信息。 |
| accountId | number | Yes | 目标系统账户的ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed. 2. System service failed to communicate with dependency module. |
| 201 | The application does not have permission to call the interface. |
| 202 | not system application. |
| 16000004 | Cannot start an invisible component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |

## terminateSelf

```TypeScript
terminateSelf(callback: AsyncCallback<void>): void
```

销毁输入法ExtensionAbility。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [InputMethodExtensionContext.destroy](arkts-ime-inputmethodextensioncontext-c.md#destroy)(callback:

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodExtensionContext-terminateSelf(callback: AsyncCallback<void>): void--><!--Device-InputMethodExtensionContext-terminateSelf(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当销毁输入法应用成功时，err为undefined；否则为错误对象。 |

## terminateSelf

```TypeScript
terminateSelf(): Promise<void>
```

销毁输入法ExtensionAbility。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [InputMethodExtensionContext.destroy](arkts-ime-inputmethodextensioncontext-c.md#destroy)()

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodExtensionContext-terminateSelf(): Promise<void>--><!--Device-InputMethodExtensionContext-terminateSelf(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

