# @ohos.app.form.formProvider(formProvider)

formProvider模块提供了获取卡片信息、更新卡片、设置卡片刷新时间等能力。该模块作为卡片提供方与卡片管理服务的桥梁，通过IPC机制与FormExtension进行通信，实现卡片的更新、信息获取等操作。适用于卡片提供方需要主动更 新卡片内容、管理卡片生命周期、获取卡片运行状态等场景，帮助开发者实现卡片的动态更新和状态管理。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.Form

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [cancelOverflow(formProvider)](arkts-form-formprovider-canceloverflow-f.md) |
| [closeFormEditAbility(formProvider)](arkts-form-formprovider-closeformeditability-f.md) |
| [getFormRect(formProvider)](arkts-form-formprovider-getformrect-f.md) |
| [getFormsInfo(formProvider)](arkts-form-formprovider-getformsinfo-f.md) |
| [getFormsInfo(formProvider)](arkts-form-formprovider-getformsinfo-f.md) |
| [getFormsInfo(formProvider)](arkts-form-formprovider-getformsinfo-f.md) |
| [getPublishedFormInfoById(formProvider)](arkts-form-formprovider-getpublishedforminfobyid-f.md) |
| [getPublishedFormInfos(formProvider)](arkts-form-formprovider-getpublishedforminfos-f.md) |
| [getPublishedRunningFormInfoById(formProvider)](arkts-form-formprovider-getpublishedrunningforminfobyid-f.md) |
| [getPublishedRunningFormInfos(formProvider)](arkts-form-formprovider-getpublishedrunningforminfos-f.md) |
| [openFormEditAbility(formProvider)](arkts-form-formprovider-openformeditability-f.md) |
| [openFormManager(formProvider)](arkts-form-formprovider-openformmanager-f.md) |
| [reloadAllForms(formProvider)](arkts-form-formprovider-reloadallforms-f.md) |
| [reloadForms(formProvider)](arkts-form-formprovider-reloadforms-f.md) |
| [requestOverflow(formProvider)](arkts-form-formprovider-requestoverflow-f.md) |
| [setFormNextRefreshTime(formProvider)](arkts-form-formprovider-setformnextrefreshtime-f.md) |
| [setFormNextRefreshTime(formProvider)](arkts-form-formprovider-setformnextrefreshtime-f.md) |
| [updateForm(formProvider)](arkts-form-formprovider-updateform-f.md) |
| [updateForm(formProvider)](arkts-form-formprovider-updateform-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [activateSceneAnimation(formProvider)](arkts-form-formprovider-activatesceneanimation-f-sys.md) |
| [deactivateSceneAnimation(formProvider)](arkts-form-formprovider-deactivatesceneanimation-f-sys.md) |
| [isRequestPublishFormSupported(formProvider)](arkts-form-formprovider-isrequestpublishformsupported-f-sys.md) |
| [isRequestPublishFormSupported(formProvider)](arkts-form-formprovider-isrequestpublishformsupported-f-sys.md) |
| [offPublishFormCrossBundleControl(formProvider)](arkts-form-formprovider-offpublishformcrossbundlecontrol-f-sys.md) |
| [onPublishFormCrossBundleControl(formProvider)](arkts-form-formprovider-onpublishformcrossbundlecontrol-f-sys.md) |
| [openFormManagerCrossBundle(formProvider)](arkts-form-formprovider-openformmanagercrossbundle-f-sys.md) |
| [requestPublishForm(formProvider)](arkts-form-formprovider-requestpublishform-f-sys.md) |
| [requestPublishForm(formProvider)](arkts-form-formprovider-requestpublishform-f-sys.md) |
| [requestPublishForm(formProvider)](arkts-form-formprovider-requestpublishform-f-sys.md) |
| [updateTemplateFormDetailInfo(formProvider)](arkts-form-formprovider-updatetemplateformdetailinfo-f-sys.md) |
<!--DelEnd-->
