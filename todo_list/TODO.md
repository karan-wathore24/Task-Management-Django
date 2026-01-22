# TODO: Fix Forget Password Functionality

## Tasks
- [x] Fix `forget_valid` view in `views.py` to properly verify user using `User.objects.get`
- [x] Add URL patterns for `forget_valid` and `upd_pss` in `urls.py`
- [x] Modify `upd_pss` view to securely retrieve user (e.g., via hidden form field)
- [x] Test the forget password flow
- [x] Verify security and functionality
