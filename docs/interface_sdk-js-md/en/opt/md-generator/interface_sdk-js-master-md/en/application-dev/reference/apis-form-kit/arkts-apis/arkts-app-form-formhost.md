# @ohos.app.form.formHost

The **formHost** module provides APIs related to the widget host, which is an application that displays the widget content and controls the position where the widget is displayed. You can use the APIs to delete, release, and update widgets installed by the same user, and obtain widget information and status.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace formHost--><!--Device-unnamed-declare namespace formHost-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { formHost } from '@kit.FormKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [acquireFormData](arkts-form-formhost-acquireformdata-f-sys.md#acquireFormData-(System-API)) |
| [acquireFormData](arkts-form-formhost-acquireformdata-f-sys.md#acquireFormData-(System-API)) |
| [acquireFormState](arkts-form-formhost-acquireformstate-f-sys.md#acquireFormState-(System-API)) |
| [acquireFormState](arkts-form-formhost-acquireformstate-f-sys.md#acquireFormState-(System-API)) |
| [addForm](arkts-form-formhost-addform-f-sys.md#addForm-(System-API)) |
| [castToNormalForm](arkts-form-formhost-casttonormalform-f-sys.md#castToNormalForm-(System-API)) |
| [castToNormalForm](arkts-form-formhost-casttonormalform-f-sys.md#castToNormalForm-(System-API)) |
| [clearRouterProxy](arkts-form-formhost-clearrouterproxy-f-sys.md#clearRouterProxy-(System-API)) |
| [clearRouterProxy](arkts-form-formhost-clearrouterproxy-f-sys.md#clearRouterProxy-(System-API)) |
| [deleteForm](arkts-form-formhost-deleteform-f-sys.md#deleteForm-(System-API)) |
| [deleteForm](arkts-form-formhost-deleteform-f-sys.md#deleteForm-(System-API)) |
| [deleteInvalidForms](arkts-form-formhost-deleteinvalidforms-f-sys.md#deleteInvalidForms-(System-API)) |
| [deleteInvalidForms](arkts-form-formhost-deleteinvalidforms-f-sys.md#deleteInvalidForms-(System-API)) |
| [disableFormsUpdate](arkts-form-formhost-disableformsupdate-f-sys.md#disableFormsUpdate-(System-API)) |
| [disableFormsUpdate](arkts-form-formhost-disableformsupdate-f-sys.md#disableFormsUpdate-(System-API)) |
| [enableFormsUpdate](arkts-form-formhost-enableformsupdate-f-sys.md#enableFormsUpdate-(System-API)) |
| [enableFormsUpdate](arkts-form-formhost-enableformsupdate-f-sys.md#enableFormsUpdate-(System-API)) |
| [getAllFormsInfo](arkts-form-formhost-getallformsinfo-f-sys.md#getAllFormsInfo-(System-API)) |
| [getAllFormsInfo](arkts-form-formhost-getallformsinfo-f-sys.md#getAllFormsInfo-(System-API)) |
| [getAllTemplateFormsInfo](arkts-form-formhost-getalltemplateformsinfo-f-sys.md#getAllTemplateFormsInfo-(System-API)) |
| [getFormIdsByFormLocation](arkts-form-formhost-getformidsbyformlocation-f-sys.md#getFormIdsByFormLocation-(System-API)) |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getFormsInfo-(System-API)) |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getFormsInfo-(System-API)) |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getFormsInfo-(System-API)) |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getFormsInfo-(System-API)) |
| [getTemplateFormsInfo](arkts-form-formhost-gettemplateformsinfo-f-sys.md#getTemplateFormsInfo-(System-API)) |
| [isSystemReady](arkts-form-formhost-issystemready-f-sys.md#isSystemReady-(System-API)) |
| [isSystemReady](arkts-form-formhost-issystemready-f-sys.md#isSystemReady-(System-API)) |
| [notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-f-sys.md#notifyFormsEnableUpdate-(System-API)) |
| [notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-f-sys.md#notifyFormsEnableUpdate-(System-API)) |
| [notifyFormsPrivacyProtected](arkts-form-formhost-notifyformsprivacyprotected-f-sys.md#notifyFormsPrivacyProtected-(System-API)) |
| [notifyFormsPrivacyProtected](arkts-form-formhost-notifyformsprivacyprotected-f-sys.md#notifyFormsPrivacyProtected-(System-API)) |
| [notifyFormsVisible](arkts-form-formhost-notifyformsvisible-f-sys.md#notifyFormsVisible-(System-API)) |
| [notifyFormsVisible](arkts-form-formhost-notifyformsvisible-f-sys.md#notifyFormsVisible-(System-API)) |
| [notifyInvisibleForms](arkts-form-formhost-notifyinvisibleforms-f-sys.md#notifyInvisibleForms-(System-API)) |
| [notifyInvisibleForms](arkts-form-formhost-notifyinvisibleforms-f-sys.md#notifyInvisibleForms-(System-API)) |
| [notifyVisibleForms](arkts-form-formhost-notifyvisibleforms-f-sys.md#notifyVisibleForms-(System-API)) |
| [notifyVisibleForms](arkts-form-formhost-notifyvisibleforms-f-sys.md#notifyVisibleForms-(System-API)) |
| [offChangeSceneAnimationState](arkts-form-formhost-offchangesceneanimationstate-f-sys.md#offChangeSceneAnimationState-(System-API)) |
| [offDeleteFormsCallback](arkts-form-formhost-offdeleteformscallback-f-sys.md#offDeleteFormsCallback-(System-API)) |
| [offFormOverflow](arkts-form-formhost-offformoverflow-f-sys.md#offFormOverflow-(System-API)) |
| [offFormUninstall](arkts-form-formhost-offformuninstall-f-sys.md#offFormUninstall-(System-API)) |
| [offGetFormRect](arkts-form-formhost-offgetformrect-f-sys.md#offGetFormRect-(System-API)) |
| [offGetLiveFormStatus](arkts-form-formhost-offgetliveformstatus-f-sys.md#offGetLiveFormStatus-(System-API)) |
| [offGetWantParamsCallback](arkts-form-formhost-offgetwantparamscallback-f-sys.md#offGetWantParamsCallback-(System-API)) |
| [offTemplateFormDetailInfoChange](arkts-form-formhost-offtemplateformdetailinfochange-f-sys.md#offTemplateFormDetailInfoChange-(System-API)) |
| [offUpdateFormsConfigCallback](arkts-form-formhost-offupdateformsconfigcallback-f-sys.md#offUpdateFormsConfigCallback-(System-API)) |
| [off_changeSceneAnimationState](arkts-form-formhost-offchangesceneanimationstate-f-sys.md) |
| [off_formOverflow](arkts-form-formhost-offformoverflow-f-sys.md) |
| off_formUninstall |
| [off_getFormRect](arkts-form-formhost-offgetformrect-f-sys.md) |
| [off_getLiveFormStatus](arkts-form-formhost-offgetliveformstatus-f-sys.md) |
| [onChangeSceneAnimationState](arkts-form-formhost-onchangesceneanimationstate-f-sys.md#onChangeSceneAnimationState-(System-API)) |
| [onDeleteFormsCallback](arkts-form-formhost-ondeleteformscallback-f-sys.md#onDeleteFormsCallback-(System-API)) |
| [onFormOverflow](arkts-form-formhost-onformoverflow-f-sys.md#onFormOverflow-(System-API)) |
| [onFormUninstall](arkts-form-formhost-onformuninstall-f-sys.md#onFormUninstall-(System-API)) |
| [onGetFormRect](arkts-form-formhost-ongetformrect-f-sys.md#onGetFormRect-(System-API)) |
| [onGetLiveFormStatus](arkts-form-formhost-ongetliveformstatus-f-sys.md#onGetLiveFormStatus-(System-API)) |
| [onGetWantParamsCallback](arkts-form-formhost-ongetwantparamscallback-f-sys.md#onGetWantParamsCallback-(System-API)) |
| [onTemplateFormDetailInfoChange](arkts-form-formhost-ontemplateformdetailinfochange-f-sys.md#onTemplateFormDetailInfoChange-(System-API)) |
| [onUpdateFormsConfigCallback](arkts-form-formhost-onupdateformsconfigcallback-f-sys.md#onUpdateFormsConfigCallback-(System-API)) |
| [on_changeSceneAnimationState](arkts-form-formhost-onchangesceneanimationstate-f-sys.md) |
| [on_formOverflow](arkts-form-formhost-onformoverflow-f-sys.md) |
| on_formUninstall |
| [on_getFormRect](arkts-form-formhost-ongetformrect-f-sys.md) |
| [on_getLiveFormStatus](arkts-form-formhost-ongetliveformstatus-f-sys.md) |
| [recoverForms](arkts-form-formhost-recoverforms-f-sys.md#recoverForms-(System-API)) |
| [recoverForms](arkts-form-formhost-recoverforms-f-sys.md#recoverForms-(System-API)) |
| [recycleForms](arkts-form-formhost-recycleforms-f-sys.md#recycleForms-(System-API)) |
| [releaseForm](arkts-form-formhost-releaseform-f-sys.md#releaseForm-(System-API)) |
| [releaseForm](arkts-form-formhost-releaseform-f-sys.md#releaseForm-(System-API)) |
| [releaseForm](arkts-form-formhost-releaseform-f-sys.md#releaseForm-(System-API)) |
| [requestForm](arkts-form-formhost-requestform-f-sys.md#requestForm-(System-API)) |
| [requestForm](arkts-form-formhost-requestform-f-sys.md#requestForm-(System-API)) |
| [requestFormWithParams](arkts-form-formhost-requestformwithparams-f-sys.md#requestFormWithParams-(System-API)) |
| [setFormsRecyclable](arkts-form-formhost-setformsrecyclable-f-sys.md#setFormsRecyclable-(System-API)) |
| [setFormsRecyclable](arkts-form-formhost-setformsrecyclable-f-sys.md#setFormsRecyclable-(System-API)) |
| [setPublishFormResult](arkts-form-formhost-setpublishformresult-f-sys.md#setPublishFormResult-(System-API)) |
| [setRouterProxy](arkts-form-formhost-setrouterproxy-f-sys.md#setRouterProxy-(System-API)) |
| [setRouterProxy](arkts-form-formhost-setrouterproxy-f-sys.md#setRouterProxy-(System-API)) |
| [shareForm](arkts-form-formhost-shareform-f-sys.md#shareForm-(System-API)) |
| [shareForm](arkts-form-formhost-shareform-f-sys.md#shareForm-(System-API)) |
| [updateFormLocation](arkts-form-formhost-updateformlocation-f-sys.md#updateFormLocation-(System-API)) |
| [updateFormLockedState](arkts-form-formhost-updateformlockedstate-f-sys.md#updateFormLockedState-(System-API)) |
| [updateFormSize](arkts-form-formhost-updateformsize-f-sys.md#updateFormSize-(System-API)) |
<!--DelEnd-->
