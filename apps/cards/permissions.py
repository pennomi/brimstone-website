""" Permission level descriptions:
 * Anonymous users can READ all data
 * TODO: Player-level users can COMMENT
 * Contributor-level users can CREATE revisions
 * Contributor-level users can UPDATE owned revisions (until approved/rejected)
 * Master-level users can UPDATE any revision (until approved/rejected)
 * Master-level users can APPROVE and REJECT any revision
 * Nobody can DELETE revisions or comments
"""

from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from apps.accounts.models import Role


class CardRevisionPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Nobody can DELETE data
        if request.method == "DELETE":
            return False
        # Anyone can READ the data
        if request.method in SAFE_METHODS:
            return True
        # But that's all unauthed users can do
        if not request.user.is_authenticated():
            return False
        # Contributor-level users have access to everything
        if request.user.role >= Role.Contributor:
            return True
        # Default to no access
        return False

    def has_object_permission(self, request, view, obj):
        # Anyone can READ the data
        if request.method in SAFE_METHODS:
            return True
        # But that's all unauthed users can do
        if not request.user.is_authenticated():
            return False
        # If the revision is approved/rejected, it's locked
        if obj.approved_at or obj.rejected_at:
            return False
        # A user can always UPDATE their own revisions
        if obj.creator == request.user:
            return True
        # A Master-level user can UPDATE anyone's revision
        if request.user.role >= Role.Master:
            return True
        # Default to no access
        return False


class CardRevisionApprovalPermission(CardRevisionPermission):
    def has_object_permission(self, request, view, obj):
        # Only Master-level users can approve or reject
        authed = request.user.is_authenticated()
        if not authed or not request.user.role == Role.Master:
            return False
        return super().has_object_permission(request, view, obj)


class CardCommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Nobody can DELETE data
        if request.method == "DELETE":
            return False
        # Anyone can READ the data
        if request.method in SAFE_METHODS:
            return True
        # Authenticated users can CREATE and UPDATE
        if request.user.is_authenticated():
            return True
        # Default to no access
        return False

    def has_object_permission(self, request, view, obj):
        # Anyone can READ the data
        if request.method in SAFE_METHODS:
            return True
        # But that's all unauthed users can do
        if not request.user.is_authenticated():
            return False
        # A user can always UPDATE their own comments
        if obj.user == request.user:
            return True
        # A Master-level user can UPDATE anyone's comment
        if request.user.role >= Role.Master:
            return True
        # Default to no access
        return False
