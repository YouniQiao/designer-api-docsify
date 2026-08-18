# @ohos.app.form.formProvider

formProvider模块提供了获取卡片信息、更新卡片、设置卡片刷新时间等能力。该模块作为卡片提供方与卡片管理服务的桥梁，通过IPC机制与FormExtension进行通信，实现卡片的更新、信息获取等操作。适用于卡片提供方需要主动更 新卡片内容、管理卡片生命周期、获取卡片运行状态等场景，帮助开发者实现卡片的动态更新和状态管理。

**起始版本：** 23

<!--Device-unnamed-declare namespace formProvider--><!--Device-unnamed-declare namespace formProvider-End-->

**系统能力：** SystemCapability.Ability.Form

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [cancelOverflow](arkts-form-formprovider-canceloverflow-f.md#canceloverflow) |
| [closeFormEditAbility](arkts-form-formprovider-closeformeditability-f.md#closeformeditability) |
| [getFormRect](arkts-form-formprovider-getformrect-f.md#getformrect) |
| [getFormsInfo](arkts-form-formprovider-getformsinfo-f.md#getformsinfo) |
| [getFormsInfo](arkts-form-formprovider-getformsinfo-f.md#getformsinfo) |
| [getFormsInfo](arkts-form-formprovider-getformsinfo-f.md#getformsinfo) |
| [getPublishedFormInfoById](arkts-form-formprovider-getpublishedforminfobyid-f.md#getpublishedforminfobyid) |
| [getPublishedFormInfos](arkts-form-formprovider-getpublishedforminfos-f.md#getpublishedforminfos) |
| [getPublishedRunningFormInfoById](arkts-form-formprovider-getpublishedrunningforminfobyid-f.md#getpublishedrunningforminfobyid) |
| [getPublishedRunningFormInfos](arkts-form-formprovider-getpublishedrunningforminfos-f.md#getpublishedrunningforminfos) |
| [openFormEditAbility](arkts-form-formprovider-openformeditability-f.md#openformeditability) |
| [openFormManager](arkts-form-formprovider-openformmanager-f.md#openformmanager) |
| [reloadAllForms](arkts-form-formprovider-reloadallforms-f.md#reloadallforms) |
| [reloadForms](arkts-form-formprovider-reloadforms-f.md#reloadforms) |
| [requestOverflow](arkts-form-formprovider-requestoverflow-f.md#requestoverflow) |
| [setFormNextRefreshTime](arkts-form-formprovider-setformnextrefreshtime-f.md#setformnextrefreshtime) |
| [setFormNextRefreshTime](arkts-form-formprovider-setformnextrefreshtime-f.md#setformnextrefreshtime) |
| [updateForm](arkts-form-formprovider-updateform-f.md#updateform) |
| [updateForm](arkts-form-formprovider-updateform-f.md#updateform) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [activateSceneAnimation](arkts-form-formprovider-activatesceneanimation-f-sys.md#activatesceneanimation系统接口) |
| [deactivateSceneAnimation](arkts-form-formprovider-deactivatesceneanimation-f-sys.md#deactivatesceneanimation系统接口) |
| [isRequestPublishFormSupported](arkts-form-formprovider-isrequestpublishformsupported-f-sys.md#isrequestpublishformsupported系统接口) |
| [isRequestPublishFormSupported](arkts-form-formprovider-isrequestpublishformsupported-f-sys.md#isrequestpublishformsupported系统接口) |
| [offPublishFormCrossBundleControl](arkts-form-formprovider-offpublishformcrossbundlecontrol-f-sys.md#offpublishformcrossbundlecontrol系统接口) |
| [onPublishFormCrossBundleControl](arkts-form-formprovider-onpublishformcrossbundlecontrol-f-sys.md#onpublishformcrossbundlecontrol系统接口) |
| [openFormManagerCrossBundle](arkts-form-formprovider-openformmanagercrossbundle-f-sys.md#openformmanagercrossbundle系统接口) |
| [requestPublishForm](arkts-form-formprovider-requestpublishform-f-sys.md#requestpublishform系统接口) |
| [requestPublishForm](arkts-form-formprovider-requestpublishform-f-sys.md#requestpublishform系统接口) |
| [requestPublishForm](arkts-form-formprovider-requestpublishform-f-sys.md#requestpublishform系统接口) |
| [updateTemplateFormDetailInfo](arkts-form-formprovider-updatetemplateformdetailinfo-f-sys.md#updatetemplateformdetailinfo系统接口) |
<!--DelEnd-->
