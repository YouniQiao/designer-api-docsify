# BundleInstaller（系统接口）

Bundle installer interface, include install uninstall recover.

**起始版本：** 9

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { installer } from 'kits/@kit.AbilityKit';
```

## addExtResource

```TypeScript
addExtResource(bundleName: string, filePaths: Array<string>): Promise<void>
```

根据给定的bundleName和hsp文件路径添加扩展资源。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.INSTALL_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| filePaths | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700301](../errorcode-bundle.md#17700301-扩展资源添加失败) |

## createAppClone

```TypeScript
createAppClone(bundleName: string, createAppCloneParam?: CreateAppCloneParam): Promise<number>
```

创建应用分身。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.INSTALL_CLONE_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| createAppCloneParam | [CreateAppCloneParam](arkts-ability-installer-createappcloneparam-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |
| [17700069](../errorcode-bundle.md#17700069-应用不支持创建分身) |

## destroyAppClone

```TypeScript
destroyAppClone(bundleName: string, appIndex: number, userId?: number): Promise<void>
```

删除应用分身。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.UNINSTALL_CLONE_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| appIndex | number | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |

## destroyAppClone

```TypeScript
destroyAppClone(bundleName: string, appIndex: number, destroyAppCloneParam?: DestroyAppCloneParam): Promise<void>
```

删除应用分身。使用Promise异步回调。

**起始版本：** 15

**需要权限：** ohos.permission.UNINSTALL_CLONE_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| appIndex | number | 是 |
| destroyAppCloneParam | [DestroyAppCloneParam](arkts-ability-installer-destroyappcloneparam-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |
| [17700062](../errorcode-bundle.md#17700062-应用设置了卸载处置规则不允许直接卸载) |

## install

```TypeScript
install(hapFilePaths: Array<string>, installParam: InstallParam, callback: AsyncCallback<void>): void
```

安装指定应用。使用callback异步回调。

> **说明：**&gt;
> 安装不同分发类型的应用需要申请相应的权限，分发类型可以参考[ApplicationInfo](arkts-ability-applicationinfo-i.md)中的
> appDistributionType字段说明。

**起始版本：** 9

**需要权限：** 
- API版本23+：ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE or (ohos.permission.INSTALL_BUNDLE and ohos.permission.INSTALL_ALLOW_DOWNGRADE)
- API版本13 - 22：ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE
- API版本10 - 12：ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE
- API版本9：ohos.permission.INSTALL_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hapFilePaths | Array & lt;string & gt; | 是 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700010](../errorcode-bundle.md#17700010-文件解析失败导致应用安装失败) |
| [17700011](../errorcode-bundle.md#17700011-签名校验失败导致应用安装失败) |
| [17700012](../errorcode-bundle.md#17700012-安装包路径无效或者文件过大导致应用安装失败) |
| [17700015](../errorcode-bundle.md#17700015-多个hap配置信息不同导致应用安装失败) |
| [17700016](../errorcode-bundle.md#17700016-系统磁盘空间不足导致应用安装失败) |
| [17700017](../errorcode-bundle.md#17700017-新安装的应用版本号低于已安装的版本号导致应用安装失败) |
| [17700018](../errorcode-bundle.md#17700018-安装失败依赖的模块不存在) |
| [17700031](../errorcode-bundle.md#17700031-overlay特征校验失败导致hap安装失败) |
| [17700036](../errorcode-bundle.md#17700036-共享库缺少allowappsharelibrary特权导致安装失败) |
| [17700039](../errorcode-bundle.md#17700039-不允许安装应用间共享库) |
| [17700041](../errorcode-bundle.md#17700041-企业设备管理不允许安装该应用) |
| [17700042](../errorcode-bundle.md#17700042-数据代理中的uri配置错误) |
| [17700043](../errorcode-bundle.md#17700043-数据代理中的权限配置错误) |
| [17700044](../errorcode-bundle.md#17700044-安装包设置的多进程配置项与系统配置项设置矛盾) |
| [17700047](../errorcode-bundle.md#17700047-要更新的应用版本没有大于当前版本) |
| [17700048](../errorcode-bundle.md#17700048-代码签名校验失败) |
| [17700050](../errorcode-bundle.md#17700050-企业mdm应用普通企业应用不允许安装) |
| [17700052](../errorcode-bundle.md#17700052-非开发者模式下不允许安装调试应用) |
| [17700054](../errorcode-bundle.md#17700054-权限校验失败导致应用安装失败) |
| [17700058](../errorcode-bundle.md#17700058-指定的应用禁止在本设备或指定用户下安装) |
| [17700066](../errorcode-bundle.md#17700066-安装失败native软件包安装失败) |
| [17700073](../errorcode-bundle.md#17700073-由于设备上存在具有相同包名称但不同签名信息的应用程序导致安装失败) |
| [17700077](../errorcode-bundle.md#17700077-安装应用失败但安装对应的预置应用成功) |
| [17700076](../errorcode-bundle.md#17700076-签名证书profile文件中的类型被限制不允许安装到当前设备中导致安装失败) |

## install

```TypeScript
install(hapFilePaths: Array<string>, callback: AsyncCallback<void>): void
```

安装指定应用。使用callback异步回调。

> **说明：**&gt;
> 安装不同分发类型的应用需要申请相应的权限，分发类型可以参考[ApplicationInfo](arkts-ability-applicationinfo-i.md)中的
> appDistributionType字段说明。

**起始版本：** 9

**需要权限：** 
- API版本23+：ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE or (ohos.permission.INSTALL_BUNDLE and ohos.permission.INSTALL_ALLOW_DOWNGRADE)
- API版本13 - 22：ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE
- API版本10 - 12：ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE
- API版本9：ohos.permission.INSTALL_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hapFilePaths | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700010](../errorcode-bundle.md#17700010-文件解析失败导致应用安装失败) |
| [17700011](../errorcode-bundle.md#17700011-签名校验失败导致应用安装失败) |
| [17700012](../errorcode-bundle.md#17700012-安装包路径无效或者文件过大导致应用安装失败) |
| [17700015](../errorcode-bundle.md#17700015-多个hap配置信息不同导致应用安装失败) |
| [17700016](../errorcode-bundle.md#17700016-系统磁盘空间不足导致应用安装失败) |
| [17700017](../errorcode-bundle.md#17700017-新安装的应用版本号低于已安装的版本号导致应用安装失败) |
| [17700018](../errorcode-bundle.md#17700018-安装失败依赖的模块不存在) |
| [17700031](../errorcode-bundle.md#17700031-overlay特征校验失败导致hap安装失败) |
| [17700036](../errorcode-bundle.md#17700036-共享库缺少allowappsharelibrary特权导致安装失败) |
| [17700039](../errorcode-bundle.md#17700039-不允许安装应用间共享库) |
| [17700041](../errorcode-bundle.md#17700041-企业设备管理不允许安装该应用) |
| [17700042](../errorcode-bundle.md#17700042-数据代理中的uri配置错误) |
| [17700043](../errorcode-bundle.md#17700043-数据代理中的权限配置错误) |
| [17700044](../errorcode-bundle.md#17700044-安装包设置的多进程配置项与系统配置项设置矛盾) |
| [17700047](../errorcode-bundle.md#17700047-要更新的应用版本没有大于当前版本) |
| [17700048](../errorcode-bundle.md#17700048-代码签名校验失败) |
| [17700050](../errorcode-bundle.md#17700050-企业mdm应用普通企业应用不允许安装) |
| [17700052](../errorcode-bundle.md#17700052-非开发者模式下不允许安装调试应用) |
| [17700054](../errorcode-bundle.md#17700054-权限校验失败导致应用安装失败) |
| [17700058](../errorcode-bundle.md#17700058-指定的应用禁止在本设备或指定用户下安装) |
| [17700066](../errorcode-bundle.md#17700066-安装失败native软件包安装失败) |
| [17700073](../errorcode-bundle.md#17700073-由于设备上存在具有相同包名称但不同签名信息的应用程序导致安装失败) |
| [17700077](../errorcode-bundle.md#17700077-安装应用失败但安装对应的预置应用成功) |
| [17700076](../errorcode-bundle.md#17700076-签名证书profile文件中的类型被限制不允许安装到当前设备中导致安装失败) |

## install

```TypeScript
install(hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>
```

安装指定应用。使用Promise异步回调。

> **说明：**&gt;
> 安装不同分发类型的应用需要申请相应的权限，分发类型可以参考[ApplicationInfo](arkts-ability-applicationinfo-i.md)中的
> appDistributionType字段说明。

**起始版本：** 9

**需要权限：** 
- API版本23+：ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE or (ohos.permission.INSTALL_BUNDLE and ohos.permission.INSTALL_ALLOW_DOWNGRADE)
- API版本13 - 22：ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE
- API版本10 - 12：ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE
- API版本9：ohos.permission.INSTALL_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hapFilePaths | Array & lt;string & gt; | 是 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700010](../errorcode-bundle.md#17700010-文件解析失败导致应用安装失败) |
| [17700011](../errorcode-bundle.md#17700011-签名校验失败导致应用安装失败) |
| [17700012](../errorcode-bundle.md#17700012-安装包路径无效或者文件过大导致应用安装失败) |
| [17700015](../errorcode-bundle.md#17700015-多个hap配置信息不同导致应用安装失败) |
| [17700016](../errorcode-bundle.md#17700016-系统磁盘空间不足导致应用安装失败) |
| [17700017](../errorcode-bundle.md#17700017-新安装的应用版本号低于已安装的版本号导致应用安装失败) |
| [17700018](../errorcode-bundle.md#17700018-安装失败依赖的模块不存在) |
| [17700031](../errorcode-bundle.md#17700031-overlay特征校验失败导致hap安装失败) |
| [17700036](../errorcode-bundle.md#17700036-共享库缺少allowappsharelibrary特权导致安装失败) |
| [17700039](../errorcode-bundle.md#17700039-不允许安装应用间共享库) |
| [17700041](../errorcode-bundle.md#17700041-企业设备管理不允许安装该应用) |
| [17700042](../errorcode-bundle.md#17700042-数据代理中的uri配置错误) |
| [17700043](../errorcode-bundle.md#17700043-数据代理中的权限配置错误) |
| [17700044](../errorcode-bundle.md#17700044-安装包设置的多进程配置项与系统配置项设置矛盾) |
| [17700047](../errorcode-bundle.md#17700047-要更新的应用版本没有大于当前版本) |
| [17700048](../errorcode-bundle.md#17700048-代码签名校验失败) |
| [17700050](../errorcode-bundle.md#17700050-企业mdm应用普通企业应用不允许安装) |
| [17700052](../errorcode-bundle.md#17700052-非开发者模式下不允许安装调试应用) |
| [17700054](../errorcode-bundle.md#17700054-权限校验失败导致应用安装失败) |
| [17700058](../errorcode-bundle.md#17700058-指定的应用禁止在本设备或指定用户下安装) |
| [17700066](../errorcode-bundle.md#17700066-安装失败native软件包安装失败) |
| [17700073](../errorcode-bundle.md#17700073-由于设备上存在具有相同包名称但不同签名信息的应用程序导致安装失败) |
| [17700077](../errorcode-bundle.md#17700077-安装应用失败但安装对应的预置应用成功) |
| [17700076](../errorcode-bundle.md#17700076-签名证书profile文件中的类型被限制不允许安装到当前设备中导致安装失败) |

## installPlugin

```TypeScript
installPlugin(hostBundleName: string, pluginFilePaths: Array<string>, pluginParam?: PluginParam): Promise<void>
```

应用安装插件。使用Promise异步回调。

**起始版本：** 19

**需要权限：** ohos.permission.INSTALL_PLUGIN_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [hostBundleName](../../apis-form-kit/arkts-apis/arkts-form-forminfo-runningforminfo-i-sys.md) | string | 是 |
| pluginFilePaths | Array & lt;string & gt; | 是 |
| pluginParam | [PluginParam](arkts-ability-installer-pluginparam-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700010](../errorcode-bundle.md#17700010-文件解析失败导致应用安装失败) |
| [17700011](../errorcode-bundle.md#17700011-签名校验失败导致应用安装失败) |
| [17700012](../errorcode-bundle.md#17700012-安装包路径无效或者文件过大导致应用安装失败) |
| [17700015](../errorcode-bundle.md#17700015-多个hap配置信息不同导致应用安装失败) |
| [17700016](../errorcode-bundle.md#17700016-系统磁盘空间不足导致应用安装失败) |
| [17700017](../errorcode-bundle.md#17700017-新安装的应用版本号低于已安装的版本号导致应用安装失败) |
| [17700048](../errorcode-bundle.md#17700048-代码签名校验失败) |
| [17700052](../errorcode-bundle.md#17700052-非开发者模式下不允许安装调试应用) |
| [17700073](../errorcode-bundle.md#17700073-由于设备上存在具有相同包名称但不同签名信息的应用程序导致安装失败) |
| [17700087](../errorcode-bundle.md#17700087-当前设备不支持安装插件) |
| [17700088](../errorcode-bundle.md#17700088-应用缺少安装插件的权限) |
| [17700089](../errorcode-bundle.md#17700089-插件的-plugindistributionids-解析失败) |
| [17700090](../errorcode-bundle.md#17700090-插件与应用之间-plugindistributionids-校验失败) |
| [17700091](../errorcode-bundle.md#17700091-插件与主体同包名) |

## installPreexistingApp

```TypeScript
installPreexistingApp(bundleName: string, userId?: number): Promise<void>
```

在指定用户下安装指定bundleName的应用。使用Promise异步回调。

> **说明：**&gt;
> 该接口不支持安装[签名证书的分发类型](arkts-ability-applicationinfo-i.md)为enterprise，enterprise_mdm和
> enterprise_normal的应用。

**起始版本：** 12

**需要权限：** ohos.permission.INSTALL_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700071](../errorcode-bundle.md#17700071-不允许企业应用安装) |
| [17700058](../errorcode-bundle.md#17700058-指定的应用禁止在本设备或指定用户下安装) |

## recover

```TypeScript
recover(bundleName: string, installParam: InstallParam, callback: AsyncCallback<void>): void
```

回滚应用到初次安装时的状态。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.INSTALL_BUNDLE or ohos.permission.RECOVER_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700073](../errorcode-bundle.md#17700073-由于设备上存在具有相同包名称但不同签名信息的应用程序导致安装失败) |
| [17700058](../errorcode-bundle.md#17700058-指定的应用禁止在本设备或指定用户下安装) |

## recover

```TypeScript
recover(bundleName: string, callback: AsyncCallback<void>): void
```

回滚应用到初次安装时的状态。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.INSTALL_BUNDLE or ohos.permission.RECOVER_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700073](../errorcode-bundle.md#17700073-由于设备上存在具有相同包名称但不同签名信息的应用程序导致安装失败) |
| [17700058](../errorcode-bundle.md#17700058-指定的应用禁止在本设备或指定用户下安装) |

## recover

```TypeScript
recover(bundleName: string, installParam?: InstallParam): Promise<void>
```

回滚应用到初次安装时的状态。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.INSTALL_BUNDLE or ohos.permission.RECOVER_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700073](../errorcode-bundle.md#17700073-由于设备上存在具有相同包名称但不同签名信息的应用程序导致安装失败) |
| [17700058](../errorcode-bundle.md#17700058-指定的应用禁止在本设备或指定用户下安装) |

## removeExtResource

```TypeScript
removeExtResource(bundleName: string, moduleNames: Array<string>): Promise<void>
```

根据给定的bundleName和moduleNames删除扩展资源。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleNames | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700302](../errorcode-bundle.md#17700302-扩展资源删除失败) |

## uninstall

```TypeScript
uninstall(bundleName: string, installParam: InstallParam, callback: AsyncCallback<void>): void
```

卸载应用。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700020](../errorcode-bundle.md#17700020-预置应用无法卸载) |
| [17700040](../errorcode-bundle.md#17700040-不允许卸载应用间共享库) |
| [17700045](../errorcode-bundle.md#17700045-企业设备管理不允许卸载该应用) |
| [17700067](../errorcode-bundle.md#17700067-卸载应用失败native软件包卸载失败) |
| [17700060](../errorcode-bundle.md#17700060-指定的应用不允许被卸载) |
| [17700062](../errorcode-bundle.md#17700062-应用设置了卸载处置规则不允许直接卸载) |

## uninstall

```TypeScript
uninstall(bundleName: string, callback: AsyncCallback<void>): void
```

卸载应用。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700020](../errorcode-bundle.md#17700020-预置应用无法卸载) |
| [17700040](../errorcode-bundle.md#17700040-不允许卸载应用间共享库) |
| [17700045](../errorcode-bundle.md#17700045-企业设备管理不允许卸载该应用) |
| [17700067](../errorcode-bundle.md#17700067-卸载应用失败native软件包卸载失败) |
| [17700060](../errorcode-bundle.md#17700060-指定的应用不允许被卸载) |

## uninstall

```TypeScript
uninstall(bundleName: string, installParam?: InstallParam): Promise<void>
```

卸载应用。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700020](../errorcode-bundle.md#17700020-预置应用无法卸载) |
| [17700040](../errorcode-bundle.md#17700040-不允许卸载应用间共享库) |
| [17700045](../errorcode-bundle.md#17700045-企业设备管理不允许卸载该应用) |
| [17700067](../errorcode-bundle.md#17700067-卸载应用失败native软件包卸载失败) |
| [17700060](../errorcode-bundle.md#17700060-指定的应用不允许被卸载) |
| [17700062](../errorcode-bundle.md#17700062-应用设置了卸载处置规则不允许直接卸载) |

## uninstall

```TypeScript
uninstall(uninstallParam: UninstallParam, callback: AsyncCallback<void>): void
```

卸载一个共享包。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uninstallParam | [UninstallParam](arkts-ability-installer-uninstallparam-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700020](../errorcode-bundle.md#17700020-预置应用无法卸载) |
| [17700037](../errorcode-bundle.md#17700037-被卸载的shared-library版本被其他应用依赖) |
| [17700038](../errorcode-bundle.md#17700038-被卸载的shared-library不存在) |

## uninstall

```TypeScript
uninstall(uninstallParam: UninstallParam): Promise<void>
```

卸载一个共享包。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uninstallParam | [UninstallParam](arkts-ability-installer-uninstallparam-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700020](../errorcode-bundle.md#17700020-预置应用无法卸载) |
| [17700037](../errorcode-bundle.md#17700037-被卸载的shared-library版本被其他应用依赖) |
| [17700038](../errorcode-bundle.md#17700038-被卸载的shared-library不存在) |

## uninstallNewPreinstalledApps

```TypeScript
uninstallNewPreinstalledApps(bundleNames: Array<string>): Promise<void>
```

批量卸载新增的预置应用。使用Promise异步回调。

**起始版本：** 24

**需要权限：** ohos.permission.UNINSTALL_BUNDLE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleNames | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## uninstallPlugin

```TypeScript
uninstallPlugin(hostBundleName: string, pluginBundleName: string, pluginParam?: PluginParam): Promise<void>
```

应用卸载插件。使用Promise异步回调。

**起始版本：** 19

**需要权限：** ohos.permission.UNINSTALL_PLUGIN_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [hostBundleName](../../apis-form-kit/arkts-apis/arkts-form-forminfo-runningforminfo-i-sys.md) | string | 是 |
| [pluginBundleName](arkts-ability-pluginbundleinfo-i.md) | string | 是 |
| pluginParam | [PluginParam](arkts-ability-installer-pluginparam-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700092](../errorcode-bundle.md#17700092-插件包名不存在) |

## uninstallUpdates

```TypeScript
uninstallUpdates(bundleName: string, installParam?: InstallParam): Promise<void>
```

对预置应用进行卸载更新，恢复到初次安装时的状态。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700045](../errorcode-bundle.md#17700045-企业设备管理不允许卸载该应用) |
| [17700057](../errorcode-bundle.md#17700057-指定的应用不是预置应用) |
| [17700060](../errorcode-bundle.md#17700060-指定的应用不允许被卸载) |
| [17700067](../errorcode-bundle.md#17700067-卸载应用失败native软件包卸载失败) |
| [17700073](../errorcode-bundle.md#17700073-由于设备上存在具有相同包名称但不同签名信息的应用程序导致安装失败) |

## updateBundleForSelf

```TypeScript
updateBundleForSelf(hapFilePaths: Array<string>, installParam: InstallParam, callback: AsyncCallback<void>): void
```

更新当前应用，仅限企业设备上的企业MDM应用调用，且传入的hapFilePaths中的hap必须都属于当前应用。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.INSTALL_SELF_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hapFilePaths | Array & lt;string & gt; | 是 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700010](../errorcode-bundle.md#17700010-文件解析失败导致应用安装失败) |
| [17700011](../errorcode-bundle.md#17700011-签名校验失败导致应用安装失败) |
| [17700012](../errorcode-bundle.md#17700012-安装包路径无效或者文件过大导致应用安装失败) |
| [17700015](../errorcode-bundle.md#17700015-多个hap配置信息不同导致应用安装失败) |
| [17700016](../errorcode-bundle.md#17700016-系统磁盘空间不足导致应用安装失败) |
| [17700017](../errorcode-bundle.md#17700017-新安装的应用版本号低于已安装的版本号导致应用安装失败) |
| [17700018](../errorcode-bundle.md#17700018-安装失败依赖的模块不存在) |
| [17700039](../errorcode-bundle.md#17700039-不允许安装应用间共享库) |
| [17700041](../errorcode-bundle.md#17700041-企业设备管理不允许安装该应用) |
| [17700042](../errorcode-bundle.md#17700042-数据代理中的uri配置错误) |
| [17700043](../errorcode-bundle.md#17700043-数据代理中的权限配置错误) |
| [17700044](../errorcode-bundle.md#17700044-安装包设置的多进程配置项与系统配置项设置矛盾) |
| [17700047](../errorcode-bundle.md#17700047-要更新的应用版本没有大于当前版本) |
| [17700048](../errorcode-bundle.md#17700048-代码签名校验失败) |
| [17700049](../errorcode-bundle.md#17700049-应用自升级时安装的应用与调用方包名不同) |
| [17700050](../errorcode-bundle.md#17700050-企业mdm应用普通企业应用不允许安装) |
| [17700051](../errorcode-bundle.md#17700051-应用自升级时调用方的签名证书profile文件中的类型不是企业mdm) |

## updateBundleForSelf

```TypeScript
updateBundleForSelf(hapFilePaths: Array<string>, callback: AsyncCallback<void>): void
```

更新当前应用，仅限企业设备上的企业MDM应用调用，且传入的hapFilePaths中的hap必须都属于当前应用。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.INSTALL_SELF_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hapFilePaths | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700010](../errorcode-bundle.md#17700010-文件解析失败导致应用安装失败) |
| [17700011](../errorcode-bundle.md#17700011-签名校验失败导致应用安装失败) |
| [17700012](../errorcode-bundle.md#17700012-安装包路径无效或者文件过大导致应用安装失败) |
| [17700015](../errorcode-bundle.md#17700015-多个hap配置信息不同导致应用安装失败) |
| [17700016](../errorcode-bundle.md#17700016-系统磁盘空间不足导致应用安装失败) |
| [17700017](../errorcode-bundle.md#17700017-新安装的应用版本号低于已安装的版本号导致应用安装失败) |
| [17700018](../errorcode-bundle.md#17700018-安装失败依赖的模块不存在) |
| [17700039](../errorcode-bundle.md#17700039-不允许安装应用间共享库) |
| [17700041](../errorcode-bundle.md#17700041-企业设备管理不允许安装该应用) |
| [17700042](../errorcode-bundle.md#17700042-数据代理中的uri配置错误) |
| [17700043](../errorcode-bundle.md#17700043-数据代理中的权限配置错误) |
| [17700044](../errorcode-bundle.md#17700044-安装包设置的多进程配置项与系统配置项设置矛盾) |
| [17700047](../errorcode-bundle.md#17700047-要更新的应用版本没有大于当前版本) |
| [17700048](../errorcode-bundle.md#17700048-代码签名校验失败) |
| [17700049](../errorcode-bundle.md#17700049-应用自升级时安装的应用与调用方包名不同) |
| [17700050](../errorcode-bundle.md#17700050-企业mdm应用普通企业应用不允许安装) |
| [17700051](../errorcode-bundle.md#17700051-应用自升级时调用方的签名证书profile文件中的类型不是企业mdm) |

## updateBundleForSelf

```TypeScript
updateBundleForSelf(hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>
```

更新当前应用，仅限企业设备上的企业MDM应用调用，且传入的hapFilePaths中的hap必须都属于当前应用。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.INSTALL_SELF_BUNDLE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hapFilePaths | Array & lt;string & gt; | 是 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700010](../errorcode-bundle.md#17700010-文件解析失败导致应用安装失败) |
| [17700011](../errorcode-bundle.md#17700011-签名校验失败导致应用安装失败) |
| [17700012](../errorcode-bundle.md#17700012-安装包路径无效或者文件过大导致应用安装失败) |
| [17700015](../errorcode-bundle.md#17700015-多个hap配置信息不同导致应用安装失败) |
| [17700016](../errorcode-bundle.md#17700016-系统磁盘空间不足导致应用安装失败) |
| [17700017](../errorcode-bundle.md#17700017-新安装的应用版本号低于已安装的版本号导致应用安装失败) |
| [17700018](../errorcode-bundle.md#17700018-安装失败依赖的模块不存在) |
| [17700039](../errorcode-bundle.md#17700039-不允许安装应用间共享库) |
| [17700041](../errorcode-bundle.md#17700041-企业设备管理不允许安装该应用) |
| [17700042](../errorcode-bundle.md#17700042-数据代理中的uri配置错误) |
| [17700043](../errorcode-bundle.md#17700043-数据代理中的权限配置错误) |
| [17700044](../errorcode-bundle.md#17700044-安装包设置的多进程配置项与系统配置项设置矛盾) |
| [17700047](../errorcode-bundle.md#17700047-要更新的应用版本没有大于当前版本) |
| [17700048](../errorcode-bundle.md#17700048-代码签名校验失败) |
| [17700049](../errorcode-bundle.md#17700049-应用自升级时安装的应用与调用方包名不同) |
| [17700050](../errorcode-bundle.md#17700050-企业mdm应用普通企业应用不允许安装) |
| [17700051](../errorcode-bundle.md#17700051-应用自升级时调用方的签名证书profile文件中的类型不是企业mdm) |
