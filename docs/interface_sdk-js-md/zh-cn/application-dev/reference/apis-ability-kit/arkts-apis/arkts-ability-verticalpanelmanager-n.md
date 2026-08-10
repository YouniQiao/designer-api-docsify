# verticalPanelManager

Defines a vertical domain panel manager.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace verticalPanelManager--><!--Device-unnamed-declare namespace verticalPanelManager-End-->

**系统能力：** SystemCapability.Ability.AppExtension.VerticalPanel

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { verticalPanelManager } from 'kits/@kit.AbilityKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [startVerticalPanel](arkts-ability-verticalpanelmanager-startverticalpanel-f-sys.md#startverticalpanel) | Starts the vertical domain picker with panel config.If the target ability is visible, you can start the target ability; If the target ability is invisible,you need to apply for permission:ohos.permission.START_INVISIBLE_ABILITY to start target invisible ability.If the caller application is in the background, it is not allowed to call this interface. |
| [startVerticalPanel](arkts-ability-verticalpanelmanager-startverticalpanel-f-sys.md#startverticalpanel-1) | Starts the vertical domain picker with panel config.If the target ability is visible, you can start the target ability; If the target ability is invisible,you need to apply for permission:ohos.permission.START_INVISIBLE_ABILITY to start target invisible ability.If the caller application is in the background, it is not allowed to call this interface. |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [PanelConfig](arkts-ability-verticalpanelmanager-panelconfig-i-sys.md) | Indicates the panel config |
| [PanelStartCallback](arkts-ability-verticalpanelmanager-panelstartcallback-i-sys.md) | The callback of start vertical panel. |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [VerticalType](arkts-ability-verticalpanelmanager-verticaltype-e-sys.md) | Provides vertical type definition. |
<!--DelEnd-->

<!--Del-->
### 常量（系统接口）

| 名称 | 说明 |
| --- | --- |
| [SOURCE_APP_BUNDLE_NAME](arkts-ability-verticalpanelmanager-con-sys.md#source_app_bundle_name) | export the const string of bundleName and provide it for sourceAppInfo. |
| [SOURCE_APP_MODULE_NAME](arkts-ability-verticalpanelmanager-con-sys.md#source_app_module_name) | export the const string of moduleName and provide it for sourceAppInfo. |
| [SOURCE_APP_ABILITY_NAME](arkts-ability-verticalpanelmanager-con-sys.md#source_app_ability_name) | export the const string of abilityName and provide it for sourceAppInfo. |
| [SOURCE_APP_WINDOW_ID](arkts-ability-verticalpanelmanager-con-sys.md#source_app_window_id) | export the const string of windowId and provide it for sourceAppInfo. |
| [SOURCE_APP_SCREEN_MODE](arkts-ability-verticalpanelmanager-con-sys.md#source_app_screen_mode) | export the const string of screenMode and provide it for sourceAppInfo. |
<!--DelEnd-->

