# @ohos.app.form.formHost

The **formHost** module provides APIs related to the widget host, which is an application that displays the widget content and controls the position where the widget is displayed. You can use the APIs to delete, release, and update widgets installed by the same user, and obtain widget information and status.

**Since:** 9

<!--Device-unnamed-declare namespace formHost--><!--Device-unnamed-declare namespace formHost-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [acquireFormData](arkts-form-formhost-acquireformdata-f-sys.md#acquireformdata) |
| [acquireFormData](arkts-form-formhost-acquireformdata-f-sys.md#acquireformdata-1) |
| [acquireFormState](arkts-form-formhost-acquireformstate-f-sys.md#acquireformstate) |
| [acquireFormState](arkts-form-formhost-acquireformstate-f-sys.md#acquireformstate-1) |
| [addForm](arkts-form-formhost-addform-f-sys.md#addform) |
| [castToNormalForm](arkts-form-formhost-casttonormalform-f-sys.md#casttonormalform) |
| [castToNormalForm](arkts-form-formhost-casttonormalform-f-sys.md#casttonormalform-1) |
| [clearRouterProxy](arkts-form-formhost-clearrouterproxy-f-sys.md#clearrouterproxy) |
| [clearRouterProxy](arkts-form-formhost-clearrouterproxy-f-sys.md#clearrouterproxy-1) |
| [deleteForm](arkts-form-formhost-deleteform-f-sys.md#deleteform) |
| [deleteForm](arkts-form-formhost-deleteform-f-sys.md#deleteform-1) |
| [deleteInvalidForms](arkts-form-formhost-deleteinvalidforms-f-sys.md#deleteinvalidforms) |
| [deleteInvalidForms](arkts-form-formhost-deleteinvalidforms-f-sys.md#deleteinvalidforms-1) |
| [disableFormsUpdate](arkts-form-formhost-disableformsupdate-f-sys.md#disableformsupdate) |
| [disableFormsUpdate](arkts-form-formhost-disableformsupdate-f-sys.md#disableformsupdate-1) |
| [enableFormsUpdate](arkts-form-formhost-enableformsupdate-f-sys.md#enableformsupdate) |
| [enableFormsUpdate](arkts-form-formhost-enableformsupdate-f-sys.md#enableformsupdate-1) |
| [getAllFormsInfo](arkts-form-formhost-getallformsinfo-f-sys.md#getallformsinfo) |
| [getAllFormsInfo](arkts-form-formhost-getallformsinfo-f-sys.md#getallformsinfo-1) |
| [getAllTemplateFormsInfo](arkts-form-formhost-getalltemplateformsinfo-f-sys.md#getalltemplateformsinfo) |
| [getFormIdsByFormLocation](arkts-form-formhost-getformidsbyformlocation-f-sys.md#getformidsbyformlocation) |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getformsinfo) |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getformsinfo-1) |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getformsinfo-2) |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getformsinfo-3) |
| [getTemplateFormsInfo](arkts-form-formhost-gettemplateformsinfo-f-sys.md#gettemplateformsinfo) |
| [isSystemReady](arkts-form-formhost-issystemready-f-sys.md#issystemready) |
| [isSystemReady](arkts-form-formhost-issystemready-f-sys.md#issystemready-1) |
| [notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-f-sys.md#notifyformsenableupdate) |
| [notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-f-sys.md#notifyformsenableupdate-1) |
| [notifyFormsPrivacyProtected](arkts-form-formhost-notifyformsprivacyprotected-f-sys.md#notifyformsprivacyprotected) |
| [notifyFormsPrivacyProtected](arkts-form-formhost-notifyformsprivacyprotected-f-sys.md#notifyformsprivacyprotected-1) |
| [notifyFormsVisible](arkts-form-formhost-notifyformsvisible-f-sys.md#notifyformsvisible) |
| [notifyFormsVisible](arkts-form-formhost-notifyformsvisible-f-sys.md#notifyformsvisible-1) |
| [notifyInvisibleForms](arkts-form-formhost-notifyinvisibleforms-f-sys.md#notifyinvisibleforms) |
| [notifyInvisibleForms](arkts-form-formhost-notifyinvisibleforms-f-sys.md#notifyinvisibleforms-1) |
| [notifyVisibleForms](arkts-form-formhost-notifyvisibleforms-f-sys.md#notifyvisibleforms) |
| [notifyVisibleForms](arkts-form-formhost-notifyvisibleforms-f-sys.md#notifyvisibleforms-1) |
| [off](arkts-form-formhost-off-f-sys.md#off) |
| [off](arkts-form-formhost-off-f-sys.md#off-1) |
| [off](arkts-form-formhost-off-f-sys.md#off-2) |
| [off](arkts-form-formhost-off-f-sys.md#off-3) |
| [off](arkts-form-formhost-off-f-sys.md#off-4) |
| [offDeleteFormsCallback](arkts-form-formhost-offdeleteformscallback-f-sys.md#offdeleteformscallback) |
| [offGetWantParamsCallback](arkts-form-formhost-offgetwantparamscallback-f-sys.md#offgetwantparamscallback) |
| [offTemplateFormDetailInfoChange](arkts-form-formhost-offtemplateformdetailinfochange-f-sys.md#offtemplateformdetailinfochange) |
| [offUpdateFormsConfigCallback](arkts-form-formhost-offupdateformsconfigcallback-f-sys.md#offupdateformsconfigcallback) |
| [on](arkts-form-formhost-on-f-sys.md#on) |
| [on](arkts-form-formhost-on-f-sys.md#on-1) |
| [on](arkts-form-formhost-on-f-sys.md#on-2) |
| [on](arkts-form-formhost-on-f-sys.md#on-3) |
| [on](arkts-form-formhost-on-f-sys.md#on-4) |
| [onDeleteFormsCallback](arkts-form-formhost-ondeleteformscallback-f-sys.md#ondeleteformscallback) |
| [onGetWantParamsCallback](arkts-form-formhost-ongetwantparamscallback-f-sys.md#ongetwantparamscallback) |
| [onTemplateFormDetailInfoChange](arkts-form-formhost-ontemplateformdetailinfochange-f-sys.md#ontemplateformdetailinfochange) |
| [onUpdateFormsConfigCallback](arkts-form-formhost-onupdateformsconfigcallback-f-sys.md#onupdateformsconfigcallback) |
| [recoverForms](arkts-form-formhost-recoverforms-f-sys.md#recoverforms) |
| [recoverForms](arkts-form-formhost-recoverforms-f-sys.md#recoverforms-1) |
| [recycleForms](arkts-form-formhost-recycleforms-f-sys.md#recycleforms) |
| [releaseForm](arkts-form-formhost-releaseform-f-sys.md#releaseform) |
| [releaseForm](arkts-form-formhost-releaseform-f-sys.md#releaseform-1) |
| [releaseForm](arkts-form-formhost-releaseform-f-sys.md#releaseform-2) |
| [requestForm](arkts-form-formhost-requestform-f-sys.md#requestform) |
| [requestForm](arkts-form-formhost-requestform-f-sys.md#requestform-1) |
| [requestFormWithParams](arkts-form-formhost-requestformwithparams-f-sys.md#requestformwithparams) |
| [setFormsRecyclable](arkts-form-formhost-setformsrecyclable-f-sys.md#setformsrecyclable) |
| [setFormsRecyclable](arkts-form-formhost-setformsrecyclable-f-sys.md#setformsrecyclable-1) |
| [setPublishFormResult](arkts-form-formhost-setpublishformresult-f-sys.md#setpublishformresult) |
| [setRouterProxy](arkts-form-formhost-setrouterproxy-f-sys.md#setrouterproxy) |
| [setRouterProxy](arkts-form-formhost-setrouterproxy-f-sys.md#setrouterproxy-1) |
| [shareForm](arkts-form-formhost-shareform-f-sys.md#shareform) |
| [shareForm](arkts-form-formhost-shareform-f-sys.md#shareform-1) |
| [updateFormLocation](arkts-form-formhost-updateformlocation-f-sys.md#updateformlocation) |
| [updateFormLockedState](arkts-form-formhost-updateformlockedstate-f-sys.md#updateformlockedstate) |
| [updateFormSize](arkts-form-formhost-updateformsize-f-sys.md#updateformsize) |
<!--DelEnd-->
