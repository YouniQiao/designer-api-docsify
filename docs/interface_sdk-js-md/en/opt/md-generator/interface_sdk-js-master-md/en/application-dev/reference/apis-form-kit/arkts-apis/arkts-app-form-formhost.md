# @ohos.app.form.formHost

The **formHost** module provides APIs related to the widget host, which is an application that displays the widget content and controls the position where the widget is displayed. You can use the APIs to delete, release, and update widgets installed by the same user, and obtain widget information and status.

**Since:** 23

<!--Device-unnamed-declare namespace formHost--><!--Device-unnamed-declare namespace formHost-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## Summary

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [acquireFormData](arkts-form-formhost-acquireformdata-f-sys.md#acquireformdata-system-api) |
| [acquireFormData](arkts-form-formhost-acquireformdata-f-sys.md#acquireformdata-system-api) |
| [acquireFormState](arkts-form-formhost-acquireformstate-f-sys.md#acquireformstate-system-api) |
| [acquireFormState](arkts-form-formhost-acquireformstate-f-sys.md#acquireformstate-system-api) |
| [addForm](arkts-form-formhost-addform-f-sys.md#addform-system-api) |
| [castToNormalForm](arkts-form-formhost-casttonormalform-f-sys.md#casttonormalform-system-api) |
| [castToNormalForm](arkts-form-formhost-casttonormalform-f-sys.md#casttonormalform-system-api) |
| [clearRouterProxy](arkts-form-formhost-clearrouterproxy-f-sys.md#clearrouterproxy-system-api) |
| [clearRouterProxy](arkts-form-formhost-clearrouterproxy-f-sys.md#clearrouterproxy-system-api) |
| [deleteForm](arkts-form-formhost-deleteform-f-sys.md#deleteform-system-api) |
| [deleteForm](arkts-form-formhost-deleteform-f-sys.md#deleteform-system-api) |
| [deleteInvalidForms](arkts-form-formhost-deleteinvalidforms-f-sys.md#deleteinvalidforms-system-api) |
| [deleteInvalidForms](arkts-form-formhost-deleteinvalidforms-f-sys.md#deleteinvalidforms-system-api) |
| [disableFormsUpdate](arkts-form-formhost-disableformsupdate-f-sys.md#disableformsupdate-system-api) |
| [disableFormsUpdate](arkts-form-formhost-disableformsupdate-f-sys.md#disableformsupdate-system-api) |
| [enableFormsUpdate](arkts-form-formhost-enableformsupdate-f-sys.md#enableformsupdate-system-api) |
| [enableFormsUpdate](arkts-form-formhost-enableformsupdate-f-sys.md#enableformsupdate-system-api) |
| [getAllFormsInfo](arkts-form-formhost-getallformsinfo-f-sys.md#getallformsinfo-system-api) |
| [getAllFormsInfo](arkts-form-formhost-getallformsinfo-f-sys.md#getallformsinfo-system-api) |
| [getAllTemplateFormsInfo](arkts-form-formhost-getalltemplateformsinfo-f-sys.md#getalltemplateformsinfo-system-api) |
| [getFormIdsByFormLocation](arkts-form-formhost-getformidsbyformlocation-f-sys.md#getformidsbyformlocation-system-api) |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getformsinfo-system-api) |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getformsinfo-system-api) |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getformsinfo-system-api) |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getformsinfo-system-api) |
| [getTemplateFormsInfo](arkts-form-formhost-gettemplateformsinfo-f-sys.md#gettemplateformsinfo-system-api) |
| [isSystemReady](arkts-form-formhost-issystemready-f-sys.md#issystemready-system-api) |
| [isSystemReady](arkts-form-formhost-issystemready-f-sys.md#issystemready-system-api) |
| [notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-f-sys.md#notifyformsenableupdate-system-api) |
| [notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-f-sys.md#notifyformsenableupdate-system-api) |
| [notifyFormsPrivacyProtected](arkts-form-formhost-notifyformsprivacyprotected-f-sys.md#notifyformsprivacyprotected-system-api) |
| [notifyFormsPrivacyProtected](arkts-form-formhost-notifyformsprivacyprotected-f-sys.md#notifyformsprivacyprotected-system-api) |
| [notifyFormsVisible](arkts-form-formhost-notifyformsvisible-f-sys.md#notifyformsvisible-system-api) |
| [notifyFormsVisible](arkts-form-formhost-notifyformsvisible-f-sys.md#notifyformsvisible-system-api) |
| [notifyInvisibleForms](arkts-form-formhost-notifyinvisibleforms-f-sys.md#notifyinvisibleforms-system-api) |
| [notifyInvisibleForms](arkts-form-formhost-notifyinvisibleforms-f-sys.md#notifyinvisibleforms-system-api) |
| [notifyVisibleForms](arkts-form-formhost-notifyvisibleforms-f-sys.md#notifyvisibleforms-system-api) |
| [notifyVisibleForms](arkts-form-formhost-notifyvisibleforms-f-sys.md#notifyvisibleforms-system-api) |
| [offChangeSceneAnimationState](arkts-form-formhost-offchangesceneanimationstate-f-sys.md#offchangesceneanimationstate) |
| [offDeleteFormsCallback](arkts-form-formhost-offdeleteformscallback-f-sys.md#offdeleteformscallback-system-api) |
| [offFormOverflow](arkts-form-formhost-offformoverflow-f-sys.md#offformoverflow) |
| [offFormUninstall](arkts-form-formhost-offformuninstall-f-sys.md#offformuninstall) |
| [offGetFormRect](arkts-form-formhost-offgetformrect-f-sys.md#offgetformrect) |
| [offGetLiveFormStatus](arkts-form-formhost-offgetliveformstatus-f-sys.md#offgetliveformstatus) |
| [offGetWantParamsCallback](arkts-form-formhost-offgetwantparamscallback-f-sys.md#offgetwantparamscallback-system-api) |
| [offTemplateFormDetailInfoChange](arkts-form-formhost-offtemplateformdetailinfochange-f-sys.md#offtemplateformdetailinfochange-system-api) |
| [offUpdateFormsConfigCallback](arkts-form-formhost-offupdateformsconfigcallback-f-sys.md#offupdateformsconfigcallback-system-api) |
| [off_changeSceneAnimationState](arkts-form-formhost-offchangesceneanimationstate-f-sys.md#offchangesceneanimationstate) |
| [off_formOverflow](arkts-form-formhost-offformoverflow-f-sys.md#offformoverflow) |
| [off_formUninstall](arkts-form-formhost-offformuninstall-f-sys.md#offformuninstall) |
| [off_getFormRect](arkts-form-formhost-offgetformrect-f-sys.md#offgetformrect) |
| [off_getLiveFormStatus](arkts-form-formhost-offgetliveformstatus-f-sys.md#offgetliveformstatus) |
| [onChangeSceneAnimationState](arkts-form-formhost-onchangesceneanimationstate-f-sys.md#onchangesceneanimationstate) |
| [onDeleteFormsCallback](arkts-form-formhost-ondeleteformscallback-f-sys.md#ondeleteformscallback-system-api) |
| [onFormOverflow](arkts-form-formhost-onformoverflow-f-sys.md#onformoverflow) |
| [onFormUninstall](arkts-form-formhost-onformuninstall-f-sys.md#onformuninstall) |
| [onGetFormRect](arkts-form-formhost-ongetformrect-f-sys.md#ongetformrect) |
| [onGetLiveFormStatus](arkts-form-formhost-ongetliveformstatus-f-sys.md#ongetliveformstatus) |
| [onGetWantParamsCallback](arkts-form-formhost-ongetwantparamscallback-f-sys.md#ongetwantparamscallback-system-api) |
| [onTemplateFormDetailInfoChange](arkts-form-formhost-ontemplateformdetailinfochange-f-sys.md#ontemplateformdetailinfochange-system-api) |
| [onUpdateFormsConfigCallback](arkts-form-formhost-onupdateformsconfigcallback-f-sys.md#onupdateformsconfigcallback-system-api) |
| [on_changeSceneAnimationState](arkts-form-formhost-onchangesceneanimationstate-f-sys.md#onchangesceneanimationstate) |
| [on_formOverflow](arkts-form-formhost-onformoverflow-f-sys.md#onformoverflow) |
| [on_formUninstall](arkts-form-formhost-onformuninstall-f-sys.md#onformuninstall) |
| [on_getFormRect](arkts-form-formhost-ongetformrect-f-sys.md#ongetformrect) |
| [on_getLiveFormStatus](arkts-form-formhost-ongetliveformstatus-f-sys.md#ongetliveformstatus) |
| [recoverForms](arkts-form-formhost-recoverforms-f-sys.md#recoverforms-system-api) |
| [recoverForms](arkts-form-formhost-recoverforms-f-sys.md#recoverforms-system-api) |
| [recycleForms](arkts-form-formhost-recycleforms-f-sys.md#recycleforms-system-api) |
| [releaseForm](arkts-form-formhost-releaseform-f-sys.md#releaseform-system-api) |
| [releaseForm](arkts-form-formhost-releaseform-f-sys.md#releaseform-system-api) |
| [releaseForm](arkts-form-formhost-releaseform-f-sys.md#releaseform-system-api) |
| [requestForm](arkts-form-formhost-requestform-f-sys.md#requestform-system-api) |
| [requestForm](arkts-form-formhost-requestform-f-sys.md#requestform-system-api) |
| [requestFormWithParams](arkts-form-formhost-requestformwithparams-f-sys.md#requestformwithparams-system-api) |
| [setFormsRecyclable](arkts-form-formhost-setformsrecyclable-f-sys.md#setformsrecyclable-system-api) |
| [setFormsRecyclable](arkts-form-formhost-setformsrecyclable-f-sys.md#setformsrecyclable-system-api) |
| [setPublishFormResult](arkts-form-formhost-setpublishformresult-f-sys.md#setpublishformresult-system-api) |
| [setRouterProxy](arkts-form-formhost-setrouterproxy-f-sys.md#setrouterproxy-system-api) |
| [setRouterProxy](arkts-form-formhost-setrouterproxy-f-sys.md#setrouterproxy-system-api) |
| [shareForm](arkts-form-formhost-shareform-f-sys.md#shareform-system-api) |
| [shareForm](arkts-form-formhost-shareform-f-sys.md#shareform-system-api) |
| [updateFormLocation](arkts-form-formhost-updateformlocation-f-sys.md#updateformlocation-system-api) |
| [updateFormLockedState](arkts-form-formhost-updateformlockedstate-f-sys.md#updateformlockedstate-system-api) |
| [updateFormSize](arkts-form-formhost-updateformsize-f-sys.md#updateformsize-system-api) |
<!--DelEnd-->
