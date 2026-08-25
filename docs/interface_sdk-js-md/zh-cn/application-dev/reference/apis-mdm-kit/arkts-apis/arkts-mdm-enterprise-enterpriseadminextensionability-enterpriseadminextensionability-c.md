# EnterpriseAdminExtensionAbility

本模块提供[企业设备管理扩展能力](../../../mdm/mdm-kit-term.md#enterpriseadminextensionability企业设备管理扩展能力)，是企业设备管理应用的核心组件。  
**主要功能**：  
- 提供设备管理应用的生命周期管理能力（激活、去激活、启动等事件）。  
- 提供应用生命周期事件监听能力（安装、卸载、启动、停止、更新）。  
- 提供系统账号管理事件监听能力（账号新增、切换、删除）。  
- 提供Kiosk模式、按键事件、日志收集、系统更新等系统级事件回调。  
- 提供策略变更事件监听能力。  
**使用场景**：企业设备管理应用开发、企业应用生命周期管理、设备安全管控、账号管理、设备运维监控等。设备管理应用需要存在一个EnterpriseAdminExtensionAbility并重写相关接口，以此具备模块提供的各项能力，比如接收由系统发送的该应用被激活或者解除激活的通知。

**起始版本：** 12

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 导入模块

```TypeScript
import { EnterpriseAdminExtensionAbility } from 'kits/@kit.MDMKit';
```

## onAccountAdded

```TypeScript
onAccountAdded(accountId: number): void
```

系统账号新增事件回调。通过接口 [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) 注册MANAGED_EVENT_ACCOUNT_ADDED事件才能收到此回调。企业设备管理场景下，设备管理应用订阅系统账号新增事件，系统账号新增事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | number | 是 |

## onAccountRemoved

```TypeScript
onAccountRemoved(accountId: number): void
```

系统账号删除事件回调。通过接口 [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) 注册MANAGED_EVENT_ACCOUNT_REMOVED事件才能收到此回调。企业设备管理场景下，设备管理应用订阅系统账号删除事件，系统账号删除事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | number | 是 |

## onAccountSwitched

```TypeScript
onAccountSwitched(accountId: number): void
```

系统账号切换事件回调。通过接口 [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) 注册MANAGED_EVENT_ACCOUNT_SWITCHED事件才能收到此回调。企业设备管理场景下，设备管理应用订阅系统账号切换事件，系统账号切换事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理 员。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | number | 是 |

## onAdminDisabled

```TypeScript
onAdminDisabled(): void
```

当前设备管理应用被解除激活后，触发该回调。企业管理员或者员工解除激活设备管理，系统通知设备管理应用已解除激活admin权限。设备管理应用可在此回调函数中通知企业管理员设备已脱管。无需注册，解除激活后默认触发该回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## onAdminEnabled

```TypeScript
onAdminEnabled(): void
```

当前设备管理应用被激活后，触发该回调。企业管理员或者员工部署并激活设备管理应用，系统通知设备管理应用已激活admin权限。设备管理应用可在此回调函数中进行初始化策略设置。无需注册，激活后默认触发该回调。与onDeviceAdminEnabled的区别：  
- onAdminEnabled：设备管理应用自身被激活时触发，用于设备管理应用初始化自己的策略。  
- onDeviceAdminEnabled：超级设备管理应用监听普通设备管理应用激活事件，用于超级设备管理应用对普通设备管理应用进行管理。  
开发者应根据应用类型和监听场景选择合适的方法：普通设备管理应用使用onAdminEnabled，超级设备管理应用监听其他应用激活时使用onDeviceAdminEnabled。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## onAdminPolicyChanged

```TypeScript
onAdminPolicyChanged(event: common.PolicyChangedEvent): void
```

策略变更事件回调。超级设备管理应用可以通过接口 [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) 注册MANAGED_EVENT_POLICIES_CHANGED事件后可接收此回调。企业设备管理场景下，当任意MDM应用调用 [策略变更上报列表](../../../mdm/mdm-kit-appendix.md#策略变更上报列表)中的接口时，系统会通知当前用户下的超级设备管理应用。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | common.PolicyChangedEvent | 是 |

## onAppStart

```TypeScript
onAppStart(bundleName: string): void
```

应用启动事件回调。通过接口 [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) 注册MANAGED_EVENT_APP_START事件才能收到此回调。企业设备管理场景下，设备管理应用订阅应用启动事件，端侧应用启动事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

## onAppStop

```TypeScript
onAppStop(bundleName: string): void
```

应用停止事件回调。通过接口 [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) 注册MANAGED_EVENT_APP_STOP事件才能收到此回调。企业设备管理场景下，设备管理应用订阅应用停止事件，端侧应用停止事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

## onBundleAdded

```TypeScript
onBundleAdded(bundleName: string): void
```

应用安装事件回调，回调中包含应用包名。通过接口 [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) 注册MANAGED_EVENT_BUNDLE_ADDED事件才能收到此回调。企业设备管理场景下，设备管理应用订阅应用安装事件，端侧应用安装事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

## onBundleAdded

```TypeScript
onBundleAdded(bundleName: string, accountId: number): void
```

应用安装事件回调，回调中包含应用包名和账号ID。通过接口 [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) 注册MANAGED_EVENT_BUNDLE_ADDED事件才能收到此回调。企业设备管理场景下，设备管理应用订阅应用安装事件，端侧应用安装事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| accountId | number | 是 |

## onBundleRemoved

```TypeScript
onBundleRemoved(bundleName: string): void
```

应用卸载事件回调，回调中包含应用包名。通过接口 [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) 注册MANAGED_EVENT_BUNDLE_REMOVED事件才能收到此回调。企业设备管理场景下，设备管理应用订阅应用卸载事件，端侧应用卸载事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

## onBundleRemoved

```TypeScript
onBundleRemoved(bundleName: string, accountId: number): void
```

应用卸载事件回调，回调中包含应用包名和账号ID。通过接口 [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) 注册MANAGED_EVENT_BUNDLE_REMOVED事件才能收到此回调。企业设备管理场景下，设备管理应用订阅应用卸载事件，端侧应用卸载事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| accountId | number | 是 |

## onBundleUpdated

```TypeScript
onBundleUpdated(bundleName: string, accountId: number): void
```

应用更新事件回调，回调中包含应用包名和用户ID。通过接口 [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) 注册MANAGED_EVENT_BUNDLE_UPDATED事件才能收到此回调。企业设备管理场景下，设备管理应用可订阅所有用户下的应用更新事件，应用更新事件触发时会通知当前用户下的设备管理应用，设备管理应用可以在此回调函数中进行事 件上报，通知主用户下的企业管理员。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| accountId | number | 是 |

## onDeviceAdminDisabled

```TypeScript
onDeviceAdminDisabled(bundleName: string): void
```

仅超级设备管理应用在普通设备管理应用被解除激活时会触发此回调。企业管理员或者员工解除激活普通设备管理应用，系统通知超级设备管理应用已解除激活admin权限。超级设备管理应用可在此回调函数中通知企业管理员设备已脱管。不需要注册，解除 激活后默认触发该回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

## onDeviceAdminEnabled

```TypeScript
onDeviceAdminEnabled(bundleName: string): void
```

仅超级设备管理应用在普通设备管理应用被激活时会触发此回调。企业管理员或者员工部署并激活普通设备管理应用，系统通知超级设备管理应用已激活admin权限。超级设备管理应用可在此回调函数中进行初始化策略设置。不需要注册，激活后默认触发该 回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

## onDeviceBootCompleted

```TypeScript
onDeviceBootCompleted(): void
```

设备开机完成事件回调。通过接口 [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) 注册MANAGED_EVENT_BOOT_COMPLETED事件才能收到此回调。企业设备管理场景下，设备管理应用订阅设备启动完成事件，端侧系统在设备开机完成后会通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业 管理员。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## onKeyEvent

```TypeScript
onKeyEvent(keyEvent: systemManager.KeyEvent): void
```

[按键事件](arkts-mdm-systemmanager-keyevent-i.md)回调。MDM应用需要通过 [systemManager.addKeyEventPolicies](arkts-mdm-systemmanager-addkeyeventpolicies-f.md)接口下发按键事件 处理策略，当系统按键事件触发时，如果事件与已下发的策略匹配，则触发该回调。回调信息[keyEvent](arkts-mdm-systemmanager-keyevent-i.md)中包含 当前发生的按键事件信息。单按键事件响应。设备单按键被触发时，[onKeyEvent](#onkeyevent)会在按下和抬起时触发两次回调事件，可由 [keyEvent](arkts-mdm-systemmanager-keyevent-i.md)中keyAction属性进行判断。 [keyEvent](arkts-mdm-systemmanager-keyevent-i.md)中keyItems属性在单按键事件中可忽略。组合按键事件响应。组合按键仅支持物理按键：电源键、音量加键、音量减键进行组合。用户按下组合键时，后按下按键的事件回调将通过 [keyEvent](arkts-mdm-systemmanager-keyevent-i.md)中的keyItems属性携带当前所有已按下的按键信息。其他与单按键事件响应逻辑一致。长按事件响应。当单个按键或组合按键被长时间按下时，[onKeyEvent](#onkeyevent)会以50ms的间隔（具体间隔时间可能因系统状态及性能而稍 有延长）被连续触发，其中每次回调事件[keyEvent](arkts-mdm-systemmanager-keyevent-i.md)的actionTime属性均与按键首次按下事件回调的 [keyEvent](arkts-mdm-systemmanager-keyevent-i.md)的actionTime属性相同。其他情况下的响应逻辑与单个按键和组合按键一致。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [keyEvent](../../apis-input-kit/arkts-apis/arkts-input-inputeventclient-keyeventdata-i-sys.md) | systemManager.KeyEvent | 是 |

## onKioskModeEntering

```TypeScript
onKioskModeEntering(bundleName: string, accountId: number): void
```

应用进入Kiosk模式回调，回调中包含应用包名和用户ID。Kiosk模式为系统层面提供的一种应用运行模式，该模式下会将设备锁定在单个应用或者一组应用运行，同时对锁屏状态、状态栏、手势操作和关键功能进行控制，防止用户在设备上启动其它应用或执行其它操作。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| accountId | number | 是 |

## onKioskModeExiting

```TypeScript
onKioskModeExiting(bundleName: string, accountId: number): void
```

应用退出Kiosk模式回调，回调中包含应用包名和用户ID。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| accountId | number | 是 |

## onLogCollected

```TypeScript
onLogCollected(result: common.Result): void
```

通过[systemManager.startCollectLog](arkts-mdm-systemmanager-startcollectlog-f.md)接口成功创建日志收集任务后， 当日志收集完成时，将触发该回调。回调中包含日志收集结果。

> **说明：**&gt;
> 日志收集成功时，必须在应用的EnterpriseAdminExtensionAbility中访问沙箱目录（/data/edm/log）获取日志，获取日志方式参考下列示例代码。应用取走日志后，建议调用
> [systemManager.finishLogCollected](arkts-mdm-systemmanager-finishlogcollected-f.md)删除已收集到的日
> 志。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | common.Result | 是 |

## onMarketAppInstallResult

```TypeScript
onMarketAppInstallResult(bundleName: string, result: common.InstallationResult): void
```

安装应用市场应用接口[bundleManager.installMarketApps](arkts-mdm-bundlemanager-installmarketapps-f.md)安装 结果回调，回调中包含应用包名和安装结果。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| result | common.InstallationResult | 是 |

## onStart

```TypeScript
onStart(): void
```

EnterpriseAdminExtensionAbility启动事件回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## onStartupGuideCompleted

```TypeScript
onStartupGuideCompleted(scene: common.StartupScene): void
```

开机向导完成事件回调。通过接口 [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) 注册MANAGED_EVENT_STARTUP_GUIDE_COMPLETED事件才能收到此回调。企业设备管理场景下，设备管理应用订阅开机向导完成事件，端侧系统在首次切换子用户完成（仅限PC）、OTA升级完成、首次开机完成开机向导 时会通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scene | common.StartupScene | 是 |

## onSystemUpdate

```TypeScript
onSystemUpdate(systemUpdateInfo: systemManager.SystemUpdateInfo): void
```

系统更新事件回调。通过接口 [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) 注册MANAGED_EVENT_SYSTEM_UPDATE事件才能收到此回调。企业设备管理场景下，设备管理应用订阅系统更新事件，端侧系统更新事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| systemUpdateInfo | systemManager.SystemUpdateInfo | 是 |

## context

```TypeScript
context: EnterpriseAdminExtensionContext
```

EnterpriseAdminExtensionAbility的上下文。继承自[ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md)。

**类型：** [EnterpriseAdminExtensionContext](arkts-mdm-enterpriseadminextensioncontext-c.md)

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager
