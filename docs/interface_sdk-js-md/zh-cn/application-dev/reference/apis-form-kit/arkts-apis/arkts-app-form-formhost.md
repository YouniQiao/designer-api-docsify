# @ohos.app.form.formHost(formHost)

formHost模块提供了卡片使用方相关接口的能力，包括对使用方同一用户下安装的卡片进行删除、释放、请求更新、获取卡片信息、状态等操作。

> **说明：**&gt;
> 本模块接口均为系统接口。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { formHost } from '@kit.FormKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [acquireFormData(formHost)](arkts-form-formhost-acquireformdata-f-sys.md) |
| [acquireFormData(formHost)](arkts-form-formhost-acquireformdata-f-sys.md) |
| [acquireFormState(formHost)](arkts-form-formhost-acquireformstate-f-sys.md) |
| [acquireFormState(formHost)](arkts-form-formhost-acquireformstate-f-sys.md) |
| [addForm(formHost)](arkts-form-formhost-addform-f-sys.md) |
| [castToNormalForm(formHost)](arkts-form-formhost-casttonormalform-f-sys.md) |
| [castToNormalForm(formHost)](arkts-form-formhost-casttonormalform-f-sys.md) |
| [clearRouterProxy(formHost)](arkts-form-formhost-clearrouterproxy-f-sys.md) |
| [clearRouterProxy(formHost)](arkts-form-formhost-clearrouterproxy-f-sys.md) |
| [deleteForm(formHost)](arkts-form-formhost-deleteform-f-sys.md) |
| [deleteForm(formHost)](arkts-form-formhost-deleteform-f-sys.md) |
| [deleteInvalidForms(formHost)](arkts-form-formhost-deleteinvalidforms-f-sys.md) |
| [deleteInvalidForms(formHost)](arkts-form-formhost-deleteinvalidforms-f-sys.md) |
| [disableFormsUpdate(formHost)](arkts-form-formhost-disableformsupdate-f-sys.md) |
| [disableFormsUpdate(formHost)](arkts-form-formhost-disableformsupdate-f-sys.md) |
| [enableFormsUpdate(formHost)](arkts-form-formhost-enableformsupdate-f-sys.md) |
| [enableFormsUpdate(formHost)](arkts-form-formhost-enableformsupdate-f-sys.md) |
| [getAllFormsInfo(formHost)](arkts-form-formhost-getallformsinfo-f-sys.md) |
| [getAllFormsInfo(formHost)](arkts-form-formhost-getallformsinfo-f-sys.md) |
| [getAllTemplateFormsInfo(formHost)](arkts-form-formhost-getalltemplateformsinfo-f-sys.md) |
| [getFormIdsByFormLocation(formHost)](arkts-form-formhost-getformidsbyformlocation-f-sys.md) |
| [getFormsInfo(formHost)](arkts-form-formhost-getformsinfo-f-sys.md) |
| [getFormsInfo(formHost)](arkts-form-formhost-getformsinfo-f-sys.md) |
| [getFormsInfo(formHost)](arkts-form-formhost-getformsinfo-f-sys.md) |
| [getFormsInfo(formHost)](arkts-form-formhost-getformsinfo-f-sys.md) |
| [getTemplateFormsInfo(formHost)](arkts-form-formhost-gettemplateformsinfo-f-sys.md) |
| [isSystemReady(formHost)](arkts-form-formhost-issystemready-f-sys.md) |
| [isSystemReady(formHost)](arkts-form-formhost-issystemready-f-sys.md) |
| [notifyFormsEnableUpdate(formHost)](arkts-form-formhost-notifyformsenableupdate-f-sys.md) |
| [notifyFormsEnableUpdate(formHost)](arkts-form-formhost-notifyformsenableupdate-f-sys.md) |
| [notifyFormsPrivacyProtected(formHost)](arkts-form-formhost-notifyformsprivacyprotected-f-sys.md) |
| [notifyFormsPrivacyProtected(formHost)](arkts-form-formhost-notifyformsprivacyprotected-f-sys.md) |
| [notifyFormsVisible(formHost)](arkts-form-formhost-notifyformsvisible-f-sys.md) |
| [notifyFormsVisible(formHost)](arkts-form-formhost-notifyformsvisible-f-sys.md) |
| [notifyInvisibleForms(formHost)](arkts-form-formhost-notifyinvisibleforms-f-sys.md) |
| [notifyInvisibleForms(formHost)](arkts-form-formhost-notifyinvisibleforms-f-sys.md) |
| [notifyVisibleForms(formHost)](arkts-form-formhost-notifyvisibleforms-f-sys.md) |
| [notifyVisibleForms(formHost)](arkts-form-formhost-notifyvisibleforms-f-sys.md) |
| [off(formHost)](arkts-form-formhost-off-f-sys.md#offformuninstall) |
| [off(formHost)](arkts-form-formhost-off-f-sys.md#offformoverflow) |
| [off(formHost)](arkts-form-formhost-off-f-sys.md#offchangesceneanimationstate) |
| [off(formHost)](arkts-form-formhost-off-f-sys.md#offgetformrect) |
| [off(formHost)](arkts-form-formhost-off-f-sys.md#offgetliveformstatus) |
| [offChangeSceneAnimationState(formHost)](arkts-form-formhost-offchangesceneanimationstate-f-sys.md) |
| [offDeleteFormsCallback(formHost)](arkts-form-formhost-offdeleteformscallback-f-sys.md) |
| [offFormOverflow(formHost)](arkts-form-formhost-offformoverflow-f-sys.md) |
| [offFormUninstall(formHost)](arkts-form-formhost-offformuninstall-f-sys.md) |
| [offGetFormRect(formHost)](arkts-form-formhost-offgetformrect-f-sys.md) |
| [offGetLiveFormStatus(formHost)](arkts-form-formhost-offgetliveformstatus-f-sys.md) |
| [offGetWantParamsCallback(formHost)](arkts-form-formhost-offgetwantparamscallback-f-sys.md) |
| [offTemplateFormDetailInfoChange(formHost)](arkts-form-formhost-offtemplateformdetailinfochange-f-sys.md) |
| [offUpdateFormsConfigCallback(formHost)](arkts-form-formhost-offupdateformsconfigcallback-f-sys.md) |
| [on(formHost)](arkts-form-formhost-on-f-sys.md#onformuninstall) |
| [on(formHost)](arkts-form-formhost-on-f-sys.md#onformoverflow) |
| [on(formHost)](arkts-form-formhost-on-f-sys.md#onchangesceneanimationstate) |
| [on(formHost)](arkts-form-formhost-on-f-sys.md#ongetformrect) |
| [on(formHost)](arkts-form-formhost-on-f-sys.md#ongetliveformstatus) |
| [onChangeSceneAnimationState(formHost)](arkts-form-formhost-onchangesceneanimationstate-f-sys.md) |
| [onDeleteFormsCallback(formHost)](arkts-form-formhost-ondeleteformscallback-f-sys.md) |
| [onFormOverflow(formHost)](arkts-form-formhost-onformoverflow-f-sys.md) |
| [onFormUninstall(formHost)](arkts-form-formhost-onformuninstall-f-sys.md) |
| [onGetFormRect(formHost)](arkts-form-formhost-ongetformrect-f-sys.md) |
| [onGetLiveFormStatus(formHost)](arkts-form-formhost-ongetliveformstatus-f-sys.md) |
| [onGetWantParamsCallback(formHost)](arkts-form-formhost-ongetwantparamscallback-f-sys.md) |
| [onTemplateFormDetailInfoChange(formHost)](arkts-form-formhost-ontemplateformdetailinfochange-f-sys.md) |
| [onUpdateFormsConfigCallback(formHost)](arkts-form-formhost-onupdateformsconfigcallback-f-sys.md) |
| [recoverForms(formHost)](arkts-form-formhost-recoverforms-f-sys.md) |
| [recoverForms(formHost)](arkts-form-formhost-recoverforms-f-sys.md) |
| [recycleForms(formHost)](arkts-form-formhost-recycleforms-f-sys.md) |
| [releaseForm(formHost)](arkts-form-formhost-releaseform-f-sys.md) |
| [releaseForm(formHost)](arkts-form-formhost-releaseform-f-sys.md) |
| [releaseForm(formHost)](arkts-form-formhost-releaseform-f-sys.md) |
| [requestForm(formHost)](arkts-form-formhost-requestform-f-sys.md) |
| [requestForm(formHost)](arkts-form-formhost-requestform-f-sys.md) |
| [requestFormWithParams(formHost)](arkts-form-formhost-requestformwithparams-f-sys.md) |
| [setFormsRecyclable(formHost)](arkts-form-formhost-setformsrecyclable-f-sys.md) |
| [setFormsRecyclable(formHost)](arkts-form-formhost-setformsrecyclable-f-sys.md) |
| [setPublishFormResult(formHost)](arkts-form-formhost-setpublishformresult-f-sys.md) |
| [setRouterProxy(formHost)](arkts-form-formhost-setrouterproxy-f-sys.md) |
| [setRouterProxy(formHost)](arkts-form-formhost-setrouterproxy-f-sys.md) |
| [shareForm(formHost)](arkts-form-formhost-shareform-f-sys.md) |
| [shareForm(formHost)](arkts-form-formhost-shareform-f-sys.md) |
| [updateFormLocation(formHost)](arkts-form-formhost-updateformlocation-f-sys.md) |
| [updateFormLockedState(formHost)](arkts-form-formhost-updateformlockedstate-f-sys.md) |
| [updateFormSize(formHost)](arkts-form-formhost-updateformsize-f-sys.md) |
<!--DelEnd-->
